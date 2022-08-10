from urllib.request import *

result=urlopen('http://www.oracle.com/technetwork/java/javase/downloads/index.html')
data=result.read(326)
print(data.decode('utf-8'))

with urlopen('http://www.oracle.com/technetwork/java/javase/downloads/index.html') as f:
    f.read(326)
    print(data.decode('utf-8'))
