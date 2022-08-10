import re
import os

os.chdir(os.path.dirname(__file__))

phone_pattern=r'1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}'
text=input('请输入待识别文件的绝对路径:')
with open(text,'r',1,'utf-8') as f:
    match=re.finditer(phone_pattern,f.read())
a=set()
with open('phone.txt','w+',1,'utf-8') as f1:
    for i in match:
        a.add(i.group(0))
    for j in a:
        f1.write(j+'\n')
