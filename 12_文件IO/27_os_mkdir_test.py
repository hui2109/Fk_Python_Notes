import os

os.chdir(os.path.dirname(__file__))

path='my_dir'
os.mkdir(path,0o755)

path='abc/xyz/wawa'
os.makedirs(path,0o755)