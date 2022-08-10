f=open('疯狂Python讲义/12_文件IO/13_readlines_test.py','r',1,'utf-8')
for i in f.readlines():
    print(i,end='')
print('')
f.close()