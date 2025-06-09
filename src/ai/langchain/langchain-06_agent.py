from langchain_community.llms import Tongyi
from langchain.agents import tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from ai.config import GlobalConfig
import os

os.environ["LANGCHAIN_TRACING_V2"] = "false"

llm = Tongyi(model_name=GlobalConfig.TY_MODEL, api_key=GlobalConfig.TY_KEY)


@tool
def multiply(input_str: str) -> int:
    """Multiply two numbers in format 'a=X, b=Y'."""
    input_str = input_str[1:-1]
    params = {k.strip(): int(v.strip())
              for k, v in [pair.split("=")
                           for pair in input_str.split(",")]}
    return params["a"] * params["b"]


tools = [multiply]

# 获取ReAct提示模板
prompt = hub.pull("hwchase17/react")

# 创建智能体
agent = create_react_agent(llm, tools, prompt)

# 创建执行器
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True  # 关键：处理解析错误
)

# 执行并自动整合结果
result = agent_executor.invoke({"input": "计算7乘以8是多少？"})
print(result["output"])
