import sys,re

mailPattern=r'([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)'\
            +'[\.][a-z]{2,3}([\.][a-z]{2})?'
text=sys.stdin.read()
it=re.finditer(mailPattern,text,re.I)
for i in it:
    print(str(i.span()) + '-->' + i.group())