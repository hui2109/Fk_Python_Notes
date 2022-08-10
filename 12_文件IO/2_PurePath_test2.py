from pathlib import *

print(PurePosixPath('info')==PurePosixPath('INFO'))
print(PureWindowsPath('info')==PureWindowsPath('INFO'))
print(PureWindowsPath('INFO') in {PureWindowsPath('info')})
print(PurePosixPath('D:') < PurePosixPath('c:'))
print(PureWindowsPath('D:') > PureWindowsPath('c:'))

print(PureWindowsPath('crazyit')==PurePosixPath('crazyit'))
# print(PureWindowsPath('crazyit')<PurePosixPath('crazyit'))

pp=PureWindowsPath('abc')
print(pp/'xyz'/'wawa')
pp=PurePosixPath('abc')
print(pp/'xyz'/'wawa')
pp2=PurePosixPath('haha','hehe')
print(pp/pp2)

pp=PureWindowsPath('abc','xyz','waawa')
a=str(pp)
print(a)
pp=PurePosixPath('abc','xyz','waawa')
print(str(pp))

