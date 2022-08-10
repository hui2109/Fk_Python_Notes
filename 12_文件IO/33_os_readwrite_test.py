import os

os.chdir(os.path.dirname(__file__))

f=os.open('abc.txt',os.O_RDWR|os.O_CREAT)
# print(f)
len1=os.write(f,'水晶潭底银鱼跃，\n'.encode('utf-8'))
len2=os.write(f,'清徐风中碧竿横。\n'.encode('utf-8'))

os.lseek(f,0,os.SEEK_SET)
data=os.read(f,len1+len2)
print(data)
print(data.decode('utf-8'))
os.close(f)