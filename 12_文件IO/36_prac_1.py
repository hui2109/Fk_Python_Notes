import fileinput
import os,sys

# sys.path.append('实用小工具')
# import 排序

os.chdir(os.path.dirname(__file__))

def my_compare(x:str):
    char_dict={}
    c_generator=(i for i in range(1,53,2))
    for j in range(97,123): 
        char_dict[chr(j)]=next(c_generator)
    d_generator=(k for k in range(2,53,2))
    for l in range(65,91): 
        char_dict[chr(l)]=next(d_generator)
    return char_dict[x]

with open('t3.txt','w+',1,'utf-8') as f :
    with fileinput.input(('t1.txt','t2.txt')) as fi:
        a=[]
        for i in fi:
            a.append(i)
        b=''.join(a)
        c=sorted(b,key=my_compare)
        f.write(''.join(c))