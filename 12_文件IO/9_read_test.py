f=open('疯狂Python讲义/12_文件IO/test.txt','r',1)
try:
    while True:
        ch=f.read(1)
        if not ch:
            print('no',ch)
            break
        print(ch,end='')
finally:
    f.close()