"""
generate  2 random csv file with one identical column atleast 1000 rows.
Read those csv using python with pandas library
Manipulting the data
"""
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
    #print(sort_salary)

    #8. Replace Values: Replace values in the location column: 'New York' with 'NYC' and 'Los Angeles' with 'LA'.
    df['city'] = df['city'].replace('Chennai', 'CI')
    #print(df)

    #9. Apply Function to Column: Convert the salary column to thousands by dividing each value by 1000.
    df['salary'] = df['salary'] / 1000
    #print(df[:5].sort_values(by='id'))

    #10. Pivot Table: Create a pivot table with department as the index and the mean salary.
    pivot_table = pd.pivot_table(df, index='department', values='salary', aggfunc='mean')
    #print(pivot_table[:5])

    #11. Merge DataFrames: Merge the DataFrame with another DataFrame containing id and phonenumber
    df2 = pd.read_csv("student.csv")
    merged_inner = pd.merge(df, df2, on='id')
    merged_left = pd.merge(df, df2, on='id', how='left')
    merged_full = pd.merge(df, df2, on='id', how='outer')
    #print(merged_full[:5])

    #12. Fill Missing Values: Fill missing values in the bonus column with 0.
    df_tempfile = pd.read_csv("temp.csv")
    fill_nan_values = df_tempfile.copy()
    fill_nan_values['phonenumber'] = fill_nan_values['phonenumber'].fillna(0)
    #print(fill_nan_values[:5])

    #13. Drop Missing Values: Remove rows with any missing values.
    drop_nan_rows = df_tempfile.dropna()
    #print(drop_nan_rows)

    #14. Change Data Type: Convert the age column to a float data type.
    change_type = df.astype({'age': 'float'})
    #print(change_type[:5])

    #15. Calculate a New Column Based on Existing Columns: Create a new column total_compensation as the sum of salary and bonus.
    df['total_compensation'] = df['salary'] + df['bonus']
    #print(df[:5])

    #16. Get Unique Values: Find unique values in the department column.
    unique_values = df['department'].unique()
    #print(unique_values)

    # 17. Create a Subset Based on Multiple Conditions: Filter rows where age is greater than 25 and salary is less than 90000.
    subset_table = df[(df['age'] > 50) & (df['salary'] < 90000)]
    #print(subset_table)

    #18. Calculate Cumulative Sum: Calculate the cumulative sum of the salary column.
    df["Cumulative salary"] = df['salary'].cumsum()
    #print(df[:5])

    #19. Remove Duplicates: Remove duplicate rows based on the name column.
    remove_duplicate = df.drop_duplicates(subset=['age', 'department'])
    #print(remove_duplicate)

    #20. Reshape DataFrame (Melt): Convert the DataFrame from wide format to long format by melting columns.
    
    pandas_melt = pd.melt(df2, id_vars=['firstname'], value_vars=['country', 'phonenumber'])
    print(pandas_melt[:5])
    print(pandas_melt[995:])