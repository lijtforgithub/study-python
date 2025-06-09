from langchain_core.prompts import ChatPromptTemplate
from ai.config import ty_chat

chat = ty_chat()
system_template = "Translate the following into {language}"

# 提示词模版
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

result = prompt_template.invoke({"language": "中文", "text": "hi"})
print(result)
print(type(result))
print(chat.invoke(result).content)
