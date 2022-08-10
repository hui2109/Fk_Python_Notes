class FkResource:
    def __init__(self,tag):
        self.tag=tag
        print('构造器,初始化资源:%s'%tag)
    def __enter__(self):
        print('[__enter__%s]:'%self.tag)
        return 'fkit'
    def __exit__(self,exc_type,exc_value,exc_traceback):
        print('[__exit__%s]:'%self.tag)

        if exc_traceback is None:
            print('没有异常时关闭资源')
        else:
            print('遇到异常时关闭资源')
            return False
with FkResource('孙悟空') as dr:
    print(dr)
    print('[with代码块]没有异常')
    
print('--------------------------------')
    
with FkResource('白骨精'):
    print('[with代码块]异常之前的代码')
    raise Exception
    print('[with代码块]~~~~~~~~~~~异常之后的代码')