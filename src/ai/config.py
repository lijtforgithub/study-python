import os
from langchain_community.chat_models.tongyi import ChatTongyi


class GlobalConfig:
    TY_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
    TY_KEY = 'sk-63aaa233142246f9a4642f5bf2552baa'
    TY_MODEL = 'qwen-max'


def ty_chat(streaming=False):
    os.environ["DASHSCOPE_API_KEY"] = GlobalConfig.TY_KEY
    return ChatTongyi(model=GlobalConfig.TY_MODEL, streaming=streaming)
