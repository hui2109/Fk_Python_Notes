from pathlib import *
import os

print(os.getcwd())
os.chdir(Path(__file__).parent)
print(os.getcwd())

print('--------------------------------')

p=Path('.')
for i in p.iterdir():
    print(i)
    
print('--------------------------------')

p=Path('.')
for j in p.glob('**/*.py'):
    print(j)
# for j in p.iterdir():
#     print(j)

print('--------------------------------')

p=Path('/Users/hui99563/Documents/01_编程学习/python/python_code/疯狂Python讲义')
for k in p.glob('**/1_PurePath_test1.py'):
    print(k)