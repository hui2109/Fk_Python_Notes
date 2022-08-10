from pathlib import *
from tkinter import N

print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('/Program Files/').drive)
print(PurePosixPath('/etc').drive)

print('--------------------------------')

print(PureWindowsPath('c:/Program Files/').root)
print(PureWindowsPath('c:Program Files/').root)
print(PurePosixPath('/etc').root)

print('--------------------------------')

print(PureWindowsPath('c:/Program Files/').anchor)
print(PureWindowsPath('c:Program Files/').anchor)
print(PurePosixPath('/etc').anchor)

print('--------------------------------')

pp=PurePath('abc/xyz/wawa/haha')
print(pp.parents[0])
print(pp.parents[1])
print(pp.parents[2])
print(pp.parents[3])
print(pp.parent)

print('--------------------------------')

print(pp.name)
pp=PurePath('abc/wawa/bb.txt')
print(pp.name)

print('--------------------------------')

pp=PurePath('abc/wawa/bb.txt.tar.zip')
print(pp.suffixes[0])
print(pp.suffixes[1])
print(pp.suffixes[2])
print(pp.suffix)
print(pp.stem)

print('--------------------------------')

pp=PureWindowsPath('abc','xyz','wawa','haha')
print(pp)
print(pp.as_posix())
# print(pp.as_uri())
pp=PureWindowsPath('d:/','Python','Python3.6')
print(pp)
print(pp.as_uri())

print('--------------------------------')

print(PurePath('a/b.py').match('*.py'))
print(PurePath('a/b/c.py').match('b/*.py'))
print(PurePath('a/b/c.py').match('a/*.py'))

print('--------------------------------')

pp=PurePosixPath('c:/abc/xyz/wawa')
print(pp.relative_to('c:/'))
print(pp.relative_to('c:/abc'))
print(pp.relative_to('c:/abc/xyz'))

print('--------------------------------')

p=PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py'))
p=PureWindowsPath('c:/')
# print(p.with_name('fkit.py'))

print('--------------------------------')

p=PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))
p=PureWindowsPath('README')
print(p.with_suffix('.txt'))