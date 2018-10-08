#coding:utf-8
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


def time_func(name):
    def new_decorate(func):
        def wrapper(n, s1, s2, s3):
            st = time.time()
            res = func(n, s1, s2) * s3
            end = time.time()
            print 'cost {}'.format(end - st)
            print 'this is tack of {}'.format(name)
            return res
        return wrapper
    return new_decorate

@time_func('kangshaoshun')
def do_something(n, a, b):
    print 'come in'
    time.sleep(n)
    res = (a + b) * b
    print 'exit'
    return res


print do_something(1, 2, 3, 4)


