import os,sys

os.chdir(os.path.dirname(__file__))

# 文件夹存在、可读、可写、可执行
ret=os.access('.',os.F_OK|os.R_OK|os.W_OK|os.X_OK)
print('os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值',ret)

# 文件存在、可读、可写，但不可执行
ret=os.access(__file__,os.F_OK)
print('os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值',ret)
ret=os.access(__file__,os.R_OK)
print('os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值',ret)
ret=os.access(__file__,os.W_OK)
print('os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值',ret)
ret=os.access(__file__,os.X_OK)
print('os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值',ret)