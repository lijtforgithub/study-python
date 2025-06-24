from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from ai.config import ty_chat

chat = ty_chat()
# 提示词模版
system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
parser = StrOutputParser()

#LCEL
chain = prompt_template | chat | parser

result = chain.invoke({"language": "中文", "text": "hello word"})
print(result)
print(type(result))
