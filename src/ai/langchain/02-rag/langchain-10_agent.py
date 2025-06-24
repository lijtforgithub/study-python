import os

import bs4
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi
from langchain_core.messages import HumanMessage
from langchain_core.tools import create_retriever_tool
from langchain_text_splitters import RecursiveCharacterTextSplitter

from ai.config import GlobalConfig

os.environ["LANGCHAIN_TRACING_V2"] = "false"


loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

llm = Tongyi(model_name=GlobalConfig.TY_MODEL, api_key=GlobalConfig.TY_KEY)
embeddings = DashScopeEmbeddings(
    # model="text-embedding-v1",
    dashscope_api_key=GlobalConfig.TY_KEY
)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)
retriever = vectorstore.as_retriever()


tool = create_retriever_tool(
    retriever,
    "blog_post_retriever",
    "Searches and returns excerpts from the Autonomous Agents blog post.",
)
tools = [tool]

prompt = hub.pull("hwchase17/react")
# agent_executor = create_react_agent(llm, tools, prompt)
agent = create_react_agent(llm, tools, prompt)

# 创建执行器
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True  # 关键：处理解析错误
)

query = "What is Task Decomposition?"

for s in agent_executor.stream(
    {"input": [HumanMessage(content=query)]},
):
    print(s)
    print("----")