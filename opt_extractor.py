#!/usr/bin/python
import argparse
import os.path
import sys
from xml.etree.ElementTree import ElementTree

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('dir', help='The man directory path in systemd source code.')

    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print args.dir, 'is not a directory'
        sys.exit(-1)

    flist = ['automount', 'exec', 'kill', 'mount', 'path', 'service', 'socket',  'swap', 'target', 'timer', 'unit']
    
    for f in flist:
        fxml = os.path.join(args.dir, 'systemd.'+f+'.xml')

        tree = ElementTree()
        tree.parse(fxml)

        print '*'*10, 'options for: ', f, '*'*10

        for x in tree.findall('.//term/varname'):
            if x.text[-1] == '=':
                print x.text[0:-1]
