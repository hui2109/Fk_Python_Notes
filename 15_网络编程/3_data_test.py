from urllib.request import *

with urlopen('http://localhost:8080/test/test', data='测试数据'.encode('utf-8')) as f:
    print(f.read().decode('utf-8'))
