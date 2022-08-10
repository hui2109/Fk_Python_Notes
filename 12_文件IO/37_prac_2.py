import sys
import os

os.chdir(os.path.dirname(__file__))

with open('my.txt','w+',1,'utf-8') as f:
    # a=sys.stdin.read()
    for i in sys.stdin:
        if i != 'exit\n':
            print('已将%s写入my.txt'%i[:-1])
            f.write(i)
        else:
            print('程序已退出')
            sys.exit(0)