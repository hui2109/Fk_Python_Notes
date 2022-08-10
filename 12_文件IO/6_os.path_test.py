import os,time
print(os.path.abspath('abc.txt'))

print(os.path.commonprefix(['/usr/lib','/usr/local/lib']))
print(os.path.commonpath(['/usr/lib','/usr/local/lib']))

print(os.path.dirname('abc/xyz/README.txt'))
print(os.path.dirname('abc/xyz'))

print(os.path.exists('abc/xyz/README.txt'))

'''获取文件最后一次被访问的时间'''   
print(os.path.getctime('./疯狂Python讲义/12_文件IO/6_os.path_test.py'))
print(time.ctime(os.path.getctime('./疯狂Python讲义/12_文件IO/6_os.path_test.py')))

'''获取文件最后一次被修改的时间''' 
print(time.ctime(os.path.getmtime('./疯狂Python讲义/12_文件IO/6_os.path_test.py')))

'''获取文件的创建时间''' 
print(time.ctime(os.path.getctime('./疯狂Python讲义/12_文件IO/6_os.path_test.py')))

'''获取文件大小''' 
print(os.path.getsize('./疯狂Python讲义/12_文件IO/6_os.path_test.py'))

print(os.path.isfile('./疯狂Python讲义/12_文件IO/6_os.path_test.py'))
print(os.path.isdir('./疯狂Python讲义/12_文件IO/6_os.path_test.py'))
print(os.path.samefile('./疯狂Python讲义/12_文件IO/6_os.path_test.py',
                        '疯狂Python讲义/12_文件IO/6_os.path_test.py'))   