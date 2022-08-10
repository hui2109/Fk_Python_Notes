import os

os.chdir(os.path.dirname(__file__))

path='my_dir'
os.rmdir(path)

path='abc/xyz/wawa'
os.removedirs(path)