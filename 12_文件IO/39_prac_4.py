import pathlib,re

dir_name=input('请输入您想提取的目录:')
phone_pattern=r'1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}'
a=set()

pp=pathlib.Path(dir_name)
def get_item(p):
    for i in p.iterdir():
        if i.is_dir():
            get_item(i)
        else:
            try:
                with open(str(i),'r',1,'utf-8') as f:
                    match=re.finditer(phone_pattern,f.read())
                with open('疯狂Python讲义/12_文件IO/phones.txt','w+',1,'utf-8') as f1:
                    for i in match:
                        a.add(i.group(0))
                    for j in a:
                        f1.write(j+'\n')
            except (UnicodeDecodeError, PermissionError):
                print('出错了',str(i))
get_item(pp)