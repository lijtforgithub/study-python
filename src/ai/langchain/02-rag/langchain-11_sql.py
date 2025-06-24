from langchain.chains.sql_database.query import create_sql_query_chain
from langchain_community.llms import Tongyi
from langchain_community.tools import QuerySQLDatabaseTool
from langchain_community.utilities import SQLDatabase

from ai.config import GlobalConfig

db = SQLDatabase.from_uri("mysql+pymysql://root:admin@localhost:3306/test")
print(db.dialect)
print(db.get_usable_table_names())
llm = Tongyi(model_name=GlobalConfig.TY_MODEL, api_key=GlobalConfig.TY_KEY)

chain = create_sql_query_chain(llm, db)
sql = chain.invoke({"question": "How many python user are there? 只返回可执行的sql部分"})
print(sql)
rs = db.run(sql)
print(rs, type(rs))

execute_query = QuerySQLDatabaseTool(db=db)
write_query = create_sql_query_chain(llm, db)
chain = write_query | execute_query
rs = chain.invoke({"question": "How many python user are there? 只返回可执行的sql部分"})
print(rs)
