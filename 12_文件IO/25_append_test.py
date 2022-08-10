import os
f=open('疯狂Python讲义/12_文件IO/z.txt','a+')
f.write('我爱Python'+os.linesep)
f.writelines((
    '土门壁甚坚，'+os.linesep,
    '杏园度亦南。'+os.linesep,
    '势异邺城下，'+os.linesep,
    '纵死时犹宽。'+os.linesep
))
