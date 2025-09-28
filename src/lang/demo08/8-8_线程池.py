from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)


def get_html(times):
    import time
    time.sleep(times)
    print(f"获取网页信息{times} 完毕")
    time.sleep(times)
    return times


task1 = executor.submit(get_html, 1)
print(task1.done())
print(task1.result())
print(task1.done())

executor.submit(get_html, 2)
executor.submit(get_html, 3)
executor.submit(get_html, 4)

executor.shutdown(wait=True)

