import os

os.chdir(os.path.dirname(__file__))

# path='my_dir'
# os.rename(path,'your_dir')

path='abc/xyz/wawa'
os.renames(path,'foo/bar/haha')