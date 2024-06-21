CREATE TABLE temp_table (
  id INT,
  product STRING,
  amount FLOAT,
  year INT,
  month INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

LOAD DATA INPATH '/tmp/catbd125/Tekle/hivql/data1/part.csv' INTO TABLE temp_table;

-- Create ORC table
CREATE TABLE partitioned_bucketed_sales_orc (
  id INT,
  product STRING,
  amount FLOAT,
  year INT,
  month INT
)
PARTITIONED BY (department STRING)
STORED AS ORC;
-----------------------
/*
CREATE TABLE partitioned_bucketed_sales_orc (
  id INT,
  product STRING,
  amount FLOAT
)
PARTITIONED BY (year INT, month INT)
STORED AS ORC;
*/

-- Insert data into ORC table
INSERT INTO TABLE partitioned_bucketed_sales_orc PARTITION (year, month)
SELECT id, product, amount, year, month FROM temp_table;

-- Drop temporary table
DROP TABLE temp_table;
