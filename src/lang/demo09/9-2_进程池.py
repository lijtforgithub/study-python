import concurrent.futures
import multiprocessing

def get_html(times):
    import time
    time.sleep(times)
    print(f"获取网页信息{times} 完毕")
    time.sleep(times)
    return times


if __name__ == '__main__':
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # concurrent.futures.ProcessPoolExecutor

    # result = pool.apply_async(get_html, args=(3,))
    # pool.close()
    # pool.join()
    # print(result.get())

    for result in pool.imap(get_html, [1, 2, 3]):
        print(result)

    print('end')
