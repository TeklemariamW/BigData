import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def load_data(connection_engine):
    # Get the directory path of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to the file
    file_path = os.path.join(current_dir, "../data/employeeT.csv")
    df = pd.read_csv(file_path)
    df.to_sql("employee_t",connection_engine, if_exists='replace', index=False)

def query_data(connection_engine):
    print("It connects properly")
    query = "select * from employee_t et limit 4"
    df = pd.read_sql(query, connection_engine)
    print(df)

if __name__ == '__main__':
    try:
        # Load environment variables from .env file
        load_dotenv()
        # Retrieve database connection details from environment variables
        db_username = os.getenv("DB_USERNAME")
        db_password = os.getenv("DB_PASSWORD")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")

        url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        sql_engine = create_engine(url)

        query_data(connection_engine=sql_engine)
        #load_data(connection_engine=sql_engine)

    except Exception as ex:
        print("NOT CONNECTED: ",ex)