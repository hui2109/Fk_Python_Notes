def square(x):
    """
    一个由于计算平方的函数
    例如
    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(-3)
    9
    >>> square(0)
    0
    """
    return x * x


class User:
    """
    定义一个代表用户的类，该类包含如下两个属性
    name - 代表用户的名字
    age - 代表用户的年龄

    例如
    >>> u=User('fkjava',9)
    >>> u.name
    'fkjava'
    >>> u.age
    9
    >>> u.say('I love Python.')
    'fkjava说：I love Python.'
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, content):
        return self.name + '说：' + content


if __name__ == '__main__':
    import doctest

    doctest.testmod()
