import pandas as pd

def read_csv():
    
    return pd.read_csv('employee.csv')

if __name__ == '__main__':
    df = read_csv()
    
    #1. select spesfic columns
    select_columns = df[['age','city','salary']]
    #print(select_columns)

    #2. Filter Rows based on Conditions: f.exp. where age is greater than 40
    filter_rows = df[df['age'] > 40]
    #print(filter_rows)

    #3. Add a New Column:Add a column named years_experience with values [2, 5, 1, 10, 7].
    import random
    new_values = [random.randrange(1, 20, 1) for i in range(1, 1001)]
    df['years_of_experience'] = new_values
    #print(df)

    #4. Rename column: Rename city column into location
    rename_column = df.rename(columns={'city':'location'})
    #print(rename_column)

    #5. Drop Columns: Remove the department column from the DataFrame.
    drop_column = df.drop(columns=['department'])
    #print(drop_column)

    #6. Group By and Aggregate:Group the data by department and calculate the mean salary and the maximum age.
    groupby_agg = df.groupby('department').agg({'salary': 'mean', 'age':'max'})
    #print(groupby_agg)

    #7. Sort Values: Sort the DataFrame based on the salary column in descending order.
    sort_salary = df.sort_values(by='salary', ascending=False)
    print(sort_salary)