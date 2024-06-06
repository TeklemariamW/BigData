import pandas as pd
from src.dataprocessing import process_data

def test_process_data():
    # Create a sample DataFrame
    data = {'column': [1, 2, 3, None, 5]}
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv('test_data.csv', index=False)
    
    # Call the process_data function
    result = process_data('test_data.csv')
    
    # Check the result
    assert result == 11  # Sum of non-missing values in the 'column' column

if __name__ == "__main__":
   
    test_process_data()

