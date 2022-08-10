import os,stat

os.chmod(__file__,stat.S_IREAD)
ret=os.access(__file__,os.W_OK)
print(ret)