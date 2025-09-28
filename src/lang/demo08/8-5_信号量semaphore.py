import threading
import time

semaphore = threading.Semaphore(value=4)


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem: threading.Semaphore):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        self.sem.release()
        print('获取网页内容成功！')


class UrlProducer(threading.Thread):
    def __init__(self, sem: threading.Semaphore):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider('http://www.baidu.com/{}'.format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    url_producer = UrlProducer(semaphore)
    url_producer.start()
