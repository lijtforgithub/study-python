# 通过生成器实现协程 生产者消费者模式

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者] 消费 %s' % n)
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者] 生产 %s' % n)
        r = c.send(n)
        print('[生产者] 消费者返回 %s' % r)


c = consumer()
producer(c)
