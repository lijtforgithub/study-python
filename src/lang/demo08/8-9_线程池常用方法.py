from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED

executor = ThreadPoolExecutor(max_workers=3)


def get_html(times):
    import time
    time.sleep(times)
    print(f"获取网页信息{times} 完毕")
    time.sleep(times)
    return times


times = [4, 2, 3]

tasks = [executor.submit(get_html, times) for times in times]
# for task in as_completed(tasks):
#     print(f"主线程中获取任务的返回值是 {task.result()}")

wait(tasks, return_when=ALL_COMPLETED)
print('wait执行完毕')

for result in executor.map(get_html, times):
    print(f"主线程中获取任务的返回值是 {result}")
