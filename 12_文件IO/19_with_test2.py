import fileinput


with fileinput.input(('疯狂Python讲义/12_文件IO/test1.txt',
                        '疯狂Python讲义/12_文件IO/info.txt')) as f:
    for line in f:
        print(line,end='')