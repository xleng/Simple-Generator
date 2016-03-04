#!/usr/bin/python
#
#   The MIT License (MIT)
#   
#   Copyright (c) 2015 John Leng
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

import sys
import os
import argparse
import StringIO
from collections import OrderedDict
from orderedloader import OrderedLoader

import yaml

import logging

from options import *


log = logging.getLogger('bc')

class UnitOption(object):
    def __init__(self, opt, val):
        self._opt = opt
        self._val = val

    def __str__(self):
        return self._opt + '=' + self._val

class UnitSection(object):
    def __init__(self, name):
        self._name = name
        self._opts = []
        self._idx = -1

    def __str__(self):
        objstr = '[' + self._name + ']\r\n'
        for opt in self._opts:
            objstr += str(opt) + '\r\n'
        return objstr

    def __iter__(self):
        return self

    def next(self):
        self._idx += 1
        if self._idx >= len(self._opts):
            self._idx = -1
            raise StopIteration

        return self._opts[self._idx]
        
    def add_opt(self, opt):
        assert isinstance(opt, UnitOption)
        self._opts.append(opt)
        

class BaseUnit(object):
    def __init__(self, uname, utype):
        self._uname = uname
        self._utype = utype
        self._sec_dicts = OrderedDict()
        self._dependency = None
        self._opt_list = [(unitOptions,'Unit'), 
                          (installOptions,'Install')] 
        if str(utype+'Options') in globals():
            self._opt_list.append( (globals()[str(utype+'Options')],utype.title()) )

    def get_name(self):
        return self._uname + '.' + self._utype

    def __str__(self):
        #unitstr = ''
        #for section in self._sec_dicts:
        #    unitstr += str(self._sec_dicts[section])
        #return unitstr
        sio = StringIO.StringIO()
        self.write(sio)
        return sio.getvalue()

    def write(self, io):
        for section in self._sec_dicts:
            io.write(str(self._sec_dicts[section]))
            io.write('\r\n')

    def validate_option(self, opt):
        for (options, sname) in self._opt_list:
            if opt in options:
                return (True, sname)
        return (False, '')

    def load_options(self, opt_dict):
        bok = True
        d = []
        for opt in opt_dict:
            valid, sname = self.validate_option(opt)
            if valid:
                #print sname, opt, opt_dict[opt]
                if sname not in self._sec_dicts:
                    self._sec_dicts[sname] = UnitSection(sname)
                self._sec_dicts[sname].add_opt(UnitOption(opt, opt_dict[opt]))
                if opt in ('Wants', 'After', 'Before'):
                    d += opt_dict[opt].split()
            else:
                log.error('Option Error: \'%s\' is not validate in %s', opt, self.get_name())
                bok = False

        if len(d) > 0:
            self._dependency = list(set(d))

        return bok

    def dependency_list(self):
        return self._dependency


class BootConfiguration(object):
    '''simple generator for systemd'''
    def __init__(self, cfgfile, gen_path):
        self._units_obj = dict()
        self._file_path = cfgfile
        self._yaml_cfg = yaml.load(open(cfgfile, 'r'), OrderedLoader)
        self._gen_path = gen_path
        #print self.yaml_cfg

    def create_unit_object(self, unit, options):
        us = unit.split('.')
        if len(us) != 2:
            log.error('Name Error: Unit name invalid: \'%s\'', unit)
            return None

        u = BaseUnit(us[0], us[1])
        if not u.load_options(options):
           return None

        return u

    def check_dependency(self):
        bok = True
        units = self._units_obj.keys()
        for u in self._units_obj.values():
            dep = u.dependency_list()
            if dep:
                for d in dep:
                    if d not in units:
                        log.error('Dependency Error: can\'t find required \'%s\' for %s', d, u.get_name())
                        bok = False

        return bok

    def write_unit(self, unit):
        open(os.path.join(self._gen_path, unit.get_name()), 'w+').write(str(unit))

    def generate(self):
        for u in self._yaml_cfg:
            unit = self.create_unit_object(u, self._yaml_cfg[u])
            if unit:
                self._units_obj[unit.get_name()] = unit 
            else:
                log.error('Can\'t create unit object, please check options for %s', u)
                return -1
               

        if not self.check_dependency():
            log.error('generate error!')
            return -1

        if not os.path.exists(self._gen_path):
            os.makedirs(self._gen_path)

        for uname in self._units_obj:
            #print 'Unit:', unit.get_name()
            #print unit
            self.write_unit(self._units_obj[uname])

        log.error('generate success!')
        return 0



        
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('file', help='The configuration file which will be used.')
    parser.add_argument('path', help='Path for the generated unit files')

    args = parser.parse_args()

    log.addHandler( logging.StreamHandler() )
    return BootConfiguration(args.file, args.path).generate()


if __name__ == '__main__':
    sys.exit(main())
