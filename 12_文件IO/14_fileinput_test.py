import fileinput
for line in fileinput.input(['疯狂Python讲义/12_文件IO/info.txt','疯狂Python讲义/12_文件IO/test1.txt']):
    print(fileinput.filename(),fileinput.filelineno(),line)
fileinput.close()