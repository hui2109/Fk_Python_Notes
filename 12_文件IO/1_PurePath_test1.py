from pathlib import *

pp=PurePath('setup.py')
print(type(pp))
pp=PurePath('crazyit','some/path','info')
print(pp)
pp=PurePath(Path('crazyit'),Path('info'))
print(pp)
pp=PureWindowsPath('crazyit','some/path','info')
print(pp)

pp=PurePath()
print(pp)

pp=PurePosixPath('/etc','/usr','lib64')
print(pp)
pp=PureWindowsPath('c:\Windows','d:info')
print(pp)

pp=PureWindowsPath('c:/Windows','/Program Files')
print(pp)

pp=PurePath('foo//bar')
print(pp)
pp=PurePath('foo/./bar')
print(pp)
pp=PurePath('foo/../bar')
print(pp)
