import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os

def load_data(connection_engine):
    # Get the directory path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to the file
    file_path = os.path.join(current_dir, "../data/employeeT.csv")
    df = pd.read_csv(file_path)
    df.to_sql("employee_t",connection_engine, if_exists='replace', index=False)

def query_data(connection_engine):
    print("It connects properly")
    #result = cur.execute('SELECT * FROM branch;')
    query = "select * from employee_t et limit 4"
    df = pd.read_sql(query, connection_engine)
    print(df)

if __name__ == '__main__':
    try:
        url = "postgresql+psycopg2://consultants:WelcomeItc%402022@ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
        sql_engine = create_engine(url)

        query_data(connection_engine=sql_engine)
        #load_data(connection_engine=sql_engine)

    except Exception as ex:
        print("NOT CONNECTED: ",ex)