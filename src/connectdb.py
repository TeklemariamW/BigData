"""
Connecting MySQL database using Python + SQLAlchemy remotely
"""
import pandas as pd
from sqlalchemy import create_engine

connection_string = 'mysql+mysqlconnector://root:root@localhost:3306/datacamp'
sql_engine = create_engine(connection_string)
#connection = sql_engine.connect()

# Creating table "Student" only once
#query = "Create table Students(Id int, firstname varchar(20),lastname varchar(30), country varchar(30),number_of_rooms int);"

query = "select * from airbnb_listings limit 3"
df = pd.read_sql_query(query, sql_engine)
print(df)


