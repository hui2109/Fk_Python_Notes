f=open('./疯狂Python讲义/12_文件IO/8_open_test.py')
print(f.encoding)
print(f.mode)
print(f.closed)
print(f.name)
print(f)

print('--------------------------------')

f2=open('./PyQt6布局/源代码/logo.jpg','rb')
# print(f2.encoding)
print(f2.mode)
print(f2.closed)
print(f2.name)
print(f2)