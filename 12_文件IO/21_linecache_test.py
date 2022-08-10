import linecache
import random
print(random.__file__)
print(linecache.getline(random.__file__,3))

print('--------------------------------')

print(linecache.getline('疯狂Python讲义/12_文件IO/21_linecache_test.py',3))
print(linecache.getline('疯狂Python讲义/12_文件IO/test1.txt',2))