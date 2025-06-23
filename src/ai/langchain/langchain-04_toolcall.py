from ai.config import ty_chat
from langchain_core.tools import tool


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b"""
    return a * b


print(multiply.description)
chat = ty_chat()

chat_with_tools = chat.bind_tools([multiply])
response = chat_with_tools.invoke("计算7乘以8的结果")

print(response)

if hasattr(response, "tool_calls"):
    for tool_call in response.tool_calls:
        if tool_call["name"] == multiply.name:
            # 仅使用参数调用
            result = multiply.invoke(tool_call["args"])
            print(f"工具调用结果：{result}")
            # 使用ToolCall调用
            print(multiply.invoke(tool_call))
else:
    print("模型直接回复：", response.content)
