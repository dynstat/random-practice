def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start


def producer(cor):
    n = 1
    while n < 100:
        cor.send(n)
        n = n * 2


@coroutine
def my_filter(num, cor):
    while True:
        n = yield
        if n < num:
            cor.send(n)


@coroutine
def printer():
    while True:
        n = yield
        print(n)


prnt = printer()
filt = my_filter(50, prnt)
producer(filt)
