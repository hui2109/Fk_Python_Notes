import tempfile,os

fp=tempfile.TemporaryFile()
print(fp.name)
fp.write('两情若是长久时，'.encode('utf-8'))
fp.write('又岂在朝朝暮暮。'.encode('utf-8'))
fp.seek(0)
print(fp.read().decode('utf-8'))
fp.close()

with tempfile.TemporaryFile() as fp:
    fp.write(b'I Love Python!')
    fp.seek(0)
    print(fp.read())
    # print(fp.read().decode())

with tempfile.TemporaryDirectory() as tempdirname:
    print('创建目录',tempdirname)