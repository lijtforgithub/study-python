import bs4
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.llms import Tongyi
from ai.config import GlobalConfig
import os

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
print(splits)
vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")


def format_docs(doc_list):
    return "\n\n".join(doc.page_content for doc in doc_list)


rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)

response = rag_chain.invoke("What is Task Decomposition?")
print(response)
