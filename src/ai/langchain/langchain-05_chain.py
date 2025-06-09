from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from ai.config import ty_chat

# 提示词模版
joke_prompt = ChatPromptTemplate.from_messages([
    ("system", "你一个会讲笑话的助手"),
    ("human", "讲一个关于{topic}的笑话")
])

chat = ty_chat()
# Runnable interface | LangChain
chain = joke_prompt | chat

print(chain.invoke({"topic": "猫"}))

str_chain = chain | StrOutputParser()
print(str_chain.invoke({"topic": "狗"}))

for chunk in str_chain.stream({"topic": "老虎"}):
    print(chunk, end="|")
