"""
Connecting MySQL database using Python + SQLAlchemy remotely
"""
import pandas as pd
from sqlalchemy import create_engine

def load_data(connection_engine):
    df = pd.read_csv('temp.csv')
    df.to_sql('students', connection_engine, if_exists='append', index=False)
    
    #Creating table "Student" only once
    #query = "Create table Students(Id int, firstname varchar(20),lastname varchar(30), country varchar(30),number_of_rooms int);"
    
def query_data(connection_engine):
    query = "select * from students limit 3"
    df = pd.read_sql_query(query, connection_engine)
    print(df)

if __name__ == '__main__':
    connection_string = 'mysql+mysqlconnector://root:root@localhost:3306/datacamp'
    sql_engine = create_engine(connection_string)

    load_data(sql_engine)
    query_data(sql_engine)








