import pandas as pd
from sqlalchemy import create_engine

connection_string = 'mysql+mysqlconnector://root:root@localhost:3306/datacamp'
sql_engine = create_engine(connection_string, echo=True)
#connection = sql_engine.connect()

#query = "select * from customers"
query = "Create table Students(Id int, firstname varchar(20),lastname varchar(30), country varchar(30),number_of_rooms int);"

df = pd.read_sql_query(query, sql_engine)

#print(df)


