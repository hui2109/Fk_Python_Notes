import os
f=open('疯狂Python讲义/12_文件IO/y.txt','wb+')
f.write(('我爱Python'+os.linesep).encode('GBK'))
f.writelines((
    ('土门壁甚坚，'+os.linesep).encode('GBK'),
    ('杏园度亦南。'+os.linesep).encode('GBK'),
    ('势异邺城下，'+os.linesep).encode('GBK'),
    ('纵死时犹宽。'+os.linesep).encode('GBK')
))

print(('我爱Python'+os.linesep).encode('GBK'))
print(('我爱Python'+os.linesep).encode('utf-8'))