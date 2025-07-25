import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

cursor = 0
while True:
    cursor, keys = r.scan(cursor=cursor, count=100)
    for key in keys:
        mem = r.memory_usage(key)
        if mem > 1024 * 1024:  # 超过 1MB 的 key
            print(f"Key: {key}, Memory: {mem} bytes")
            r.delete(key)
    if cursor == 0:
        break