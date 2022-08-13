from cgitb import reset
from unittest import result
from urllib.parse import *

result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)

print('--------------------------------')

print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机:', result.hostname)
print('端口:', result.port)
print('资源路径:', result.path, result[2])
print('参数:', result.params, result[3])
print('查询字符串:', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())

print('--------------------------------')

result = urlunparse(('http', 'www.crazyit.org:80',
                     'index.php', 'yeeku', 'name=fkit', 'frag'))
print(result)

print('--------------------------------')

result = urlparse('//www.crazyit.org:80/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])

print('--------------------------------')

result = urlparse('www.crazyit.org/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])

print('--------------------------------')

result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
print(urlencode(result))

result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
print(urlencode(result))

print('--------------------------------')

result = urljoin('http://crazyit.org/users/login.html', 'help.html')
print(result)
result = urljoin('http://crazyit.org/users/login.html', 'book/list.html')
print(result)

result = urljoin('http://crazyit.org/users/login.html', '/help.html')
print(result)

result = urljoin('http://crazyit.org/users/login.html', '//help.html')
print(result)
