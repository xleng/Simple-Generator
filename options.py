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

execOptions= (
'WorkingDirectory',
'RootDirectory',
'User',
'Group',
'SupplementaryGroups',
'Nice',
'OOMScoreAdjust',
'IOSchedulingClass',
'IOSchedulingPriority',
'CPUSchedulingPolicy',
'CPUSchedulingPriority',
'CPUSchedulingResetOnFork',
'CPUAffinity',
'UMask',
'Environment',
'EnvironmentFile',
'StandardInput',
'StandardOutput',
'StandardError',
'TTYPath',
'TTYReset',
'TTYVHangup',
'TTYVTDisallocate',
'SyslogIdentifier',
'SyslogFacility',
'SyslogLevel',
'SyslogLevelPrefix',
'TimerSlackNSec',
'LimitCPU',
'LimitFSIZE',
'LimitDATA',
'LimitSTACK',
'LimitCORE',
'LimitRSS',
'LimitNOFILE',
'LimitAS',
'LimitNPROC',
'LimitMEMLOCK',
'LimitLOCKS',
'LimitSIGPENDING',
'LimitMSGQUEUE',
'LimitNICE',
'LimitRTPRIO',
'LimitRTTIME',
'PAMName',
'TCPWrapName',
'CapabilityBoundingSet',
'SecureBits',
'Capabilities',
'ReadWriteDirectories',
'ReadOnlyDirectories',
'InaccessibleDirectories',
'PrivateTmp',
'PrivateNetwork',
'MountFlags',
'UtmpIdentifier',
'IgnoreSIGPIPE',
'NoNewPrivileges',
'SystemCallFilter'
)


killOptions = (
'KillMode',
'KillSignal',
'SendSIGHUP',
'SendSIGKILL'
)

mountOptions = (
'What',
'Where',
'Type',
'Options',
'DirectoryMode',
'TimeoutSec'
)

serviceOptions= (
#service section
'Type',
'RemainAfterExit',
'GuessMainPID',
'PIDFile',
'BusName',
'ExecStart',
'ExecStartPre',
'ExecStartPost',
'ExecReload',
'ExecStop',
'ExecStopPost',
'RestartSec',
'TimeoutStartSec',
'TimeoutStopSec',
'TimeoutSec',
'WatchdogSec',
'Restart',
'SuccessExitStatus',
'RestartPreventExitStatus',
'PermissionsStartOnly',
'RootDirectoryStartOnly',
'NonBlocking',
'NotifyAccess',
'Sockets',
'StartLimitInterval',
'StartLimitBurst',
'StartLimitAction',
'SysVStartPriority',
'FsckPassNo'
)

socketOptions = (
'ListenStream',
'ListenDatagram',
'ListenSequentialPacket',
'ListenFIFO',
'ListenSpecial',
'ListenNetlink',
'ListenMessageQueue',
'BindIPv6Only',
'Backlog',
'BindToDevice',
'DirectoryMode',
'SocketMode',
'Accept',
'MaxConnections',
'KeepAlive',
'Priority',
'ReceiveBuffer',
'SendBuffer',
'IPTOS',
'IPTTL',
'Mark',
'ReusePort',
'SmackLabel',
'SmackLabelIPIn',
'SmackLabelIPOut',
'PipeSize',
'MessageQueueMaxMessages',
'MessageQueueMessageSize',
'FreeBind',
'Transparent',
'Broadcast',
'PassCredentials',
'PassSecurity',
'TCPCongestion',
'ExecStartPre',
'ExecStartPost',
'ExecStopPre',
'ExecStopPost',
'TimeoutSec',
'Service'
)

unitOptions= (
#unit section
'Description',
'Documentation',
'Requires',
'RequiresOverridable',
'Requisite',
'RequisiteOverridable',
'Wants',
'BindsTo',
'PartOf',
'Conflicts',
'Before',
'After',
'OnFailure',
'PropagatesReloadTo',
'ReloadPropagatedFrom',
'RequiresMountsFor',
'OnFailureIsolate',
'IgnoreOnIsolate',
'IgnoreOnSnapshot',
'StopWhenUnneeded',
'RefuseManualStart',
'RefuseManualStop',
'AllowIsolate',
'DefaultDependencies',
'JobTimeoutSec',
'ConditionPathExists',
'ConditionPathExistsGlob',
'ConditionPathIsDirectory',
'ConditionPathIsSymbolicLink',
'ConditionPathIsMountPoint',
'ConditionPathIsReadWrite',
'ConditionDirectoryNotEmpty',
'ConditionFileNotEmpty',
'ConditionFileIsExecutable',
'ConditionKernelCommandLine',
'ConditionVirtualization',
'ConditionSecurity',
'ConditionCapability',
'ConditionHost',
'ConditionACPower',
'ConditionNull',
'SourcePath'
)

installOptions = (
#install section
'Alias',
'WantedBy',
'RequiredBy',
'Also',
)





