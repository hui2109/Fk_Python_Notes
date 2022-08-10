# 指定使用UTF-8字符集读取文件内容
f=open('疯狂Python讲义/12_文件IO/15_for_file.py','r',1,'utf-8')
# 使用for-in循环遍历文件对象
for line in f :
    print(line,end='')
f.close()

print('--------------------------------')

print(list(open('疯狂Python讲义/12_文件IO/15_for_file.py','r',1,'utf-8')))