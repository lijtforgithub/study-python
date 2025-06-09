from datetime import datetime
from json import JSONDecodeError
from ai.config import GlobalConfig, ty_chat

from langchain_community.llms.tongyi import Tongyi
from langchain_core.tools import tool
from langchain_core.exceptions import OutputParserException
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import render_text_description
from langchain_core.utils.json import parse_json_markdown


@tool
def book_rooms(start_time: str, end_time: str) -> str:
    """
	预定会议室

	Parameters:
    start_time: 格式为 %Y-%m-%d %H:%M:00。且%M只能为00或者30。
	end_time: 格式为 %Y-%m-%d %H:%M:00。且%M只能为00或者30。

	Example:
    >>> book_rooms("2024-3-1 12:00:00", "2024-3-1 12:30:00")
    """
    # 一些预定会议室的动作
    return "预定成功"


tools = [book_rooms]
rendered_tools = render_text_description(tools)

system_prompt = f"""You are an assistant that has access to the following set of tools. Here are the names and descriptions for each tool:

{rendered_tools}

Given the user input, return the name and input of the tool to use. Return your response as a JSON blob with 'name' and 'arguments' keys."""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt),
     ("ai",
      f"Today's date is {datetime.now().strftime('%Y-%m-%d')}. If the user's time is unclear, they can inquire multiple times."),
     ("user", "{input}")]
)


def parse_json(response: AIMessage):
    text = response.content
    text = text.strip()
    try:
        return parse_json_markdown(text)
    except JSONDecodeError as e:
        msg = f"Invalid json output: {text}"
        raise OutputParserException(msg, llm_output=text) from e

ty_chat()

llm = Tongyi(
    model_name=GlobalConfig.TY_MODEL,  # 或其他通义模型
    alibaba_api_key=GlobalConfig.TY_KEY,
    temperature=0.7,
    top_p=0.9
)
chain = prompt | llm | parse_json

print(chain.invoke({"input": "订今天下午3点，时长半小时的会议室"}))
