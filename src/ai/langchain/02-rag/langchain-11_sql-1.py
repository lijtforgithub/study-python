from operator import itemgetter

from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.llms import Tongyi
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from ai.config import GlobalConfig

db = SQLDatabase.from_uri("mysql+pymysql://root:admin@localhost:3306/test")
llm = Tongyi(model_name=GlobalConfig.TY_MODEL, api_key=GlobalConfig.TY_KEY)

execute_query = QuerySQLDatabaseTool(db=db)
write_query = create_sql_query_chain(llm, db)

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)

chain = (
    RunnablePassthrough.assign(query=write_query).assign(
        result=itemgetter("query") | execute_query
    )
    | answer_prompt
    | llm
    | StrOutputParser()
)

response = chain.invoke({"question": "How many python user are there? 只返回可执行的sql部分"})
print(response)