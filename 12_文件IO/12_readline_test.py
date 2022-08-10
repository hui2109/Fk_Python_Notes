f=open('疯狂Python讲义/12_文件IO/12_readline_test.py','r',1,'utf-8')
while True:
    line=f.readline()
    if not line:
        print('')
        break
    print(line,end='')
f.close()