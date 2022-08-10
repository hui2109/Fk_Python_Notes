f=open('疯狂Python讲义/12_文件IO/test.txt','rb')
print(f.read().decode('gbk'))
f.close()

print('--------------------------------')

f=open('疯狂Python讲义/12_文件IO/test.txt','r',1,'GBK')
while True:
    ch=f.read(1)
    if not ch:
        print('')
        break    
    print(ch,end='')
f.close()

print('--------------------------------')

# f=open('PyQt6布局/源代码/logo.jpg','rb')
# print(f.read())
# f.close()