from langchain_core.output_parsers import StrOutputParser

from ai.config import ty_chat
from langchain_core.messages import HumanMessage

chat = ty_chat()
response = chat.invoke([HumanMessage(content="你好，你是谁？")])
print(response)
print(type(response))
print(response.content)

# 输出解析器
parser = StrOutputParser()
print(parser.invoke(response))

# 流式输出
chat = ty_chat(streaming=True)
for chunk in chat.stream([HumanMessage(content="写一首包含李敬堂的藏头诗")]):
    print(chunk.content, end="", flush=True)
