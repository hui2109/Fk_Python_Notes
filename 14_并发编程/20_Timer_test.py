from threading import Timer

def hello():
    print('hello world!')
t=Timer(10,hello)
t.start()