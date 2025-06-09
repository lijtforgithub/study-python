from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
result = remote_chain.invoke({"language": "英语", "text": "人工智能好学吗"})
print(result)
