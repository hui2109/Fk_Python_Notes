from pathlib import *
import fnmatch

for file in Path('./疯狂Python讲义/12_文件IO').iterdir():
    if fnmatch.fnmatch(file,'*_test.py'):
        print(file)
        
print('--------------------------------')
         
for file in Path('./疯狂Python讲义/12_文件IO').iterdir():
    if fnmatch.fnmatchcase(str(file),'*_test.py'):
        print(file)
        
print('--------------------------------')
        
names=['a.py','b.py','c.py','d.py']
sub=fnmatch.filter(names,'[a-c].py')
print(sub)

print('--------------------------------')

print(fnmatch.translate('?.py'))
print(fnmatch.translate('[ac].py'))
print(fnmatch.translate('[a-c].py'))