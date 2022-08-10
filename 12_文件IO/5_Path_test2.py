from pathlib import *
p=Path('./疯狂Python讲义/12_文件IO/a_test.txt')
result=p.write_text('''        有一个美丽的新世界，
        它在远方等我，
        那里有天真的孩子，
        还有姑娘的酒窝。''',encoding='utf-8')
print(result)

print('--------------------------------')

content=p.read_text(encoding='utf-8')
print(content)

print('--------------------------------')

bb=p.read_bytes()
print(bb)