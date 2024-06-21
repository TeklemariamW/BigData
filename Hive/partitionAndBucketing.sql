/*
Partitioning in Hive organizes data into directories based on column values, 
optimizing data retrieval and management.

Bucketing organizes data within partitions into smaller files based on hash values, 
improving query performance, especially for joins.

Use Cases: Partitioning and bucketing are essential techniques in Hive 
for optimizing performance, managing large datasets efficiently, and improving query 
execution times, especially in data warehousing and analytical processing scenarios.

sudo -u hdfs hdfs dfs -ls /warehouse/tablespace/managed/hive/uttam123.db/partitioned_bucketed_sales
*/

--Creating a Partitioned Table:
CREATE TABLE sales1 (
    transaction_id INT,
    amount DECIMAL(10, 2),
    transaction_date STRING
)
PARTITIONED BY (year INT, month INT);

--Loading Data into Partitions:
-- Load data into the partition for year 2023 and month 1
LOAD DATA INPATH 'hdfs://path/to/data/year=2023/month=01' INTO TABLE sales PARTITION (year=2023, month=1);
--or
INSERT INTO TABLE sales1 PARTITION (year=2023, month=2)
SELECT transaction_id, amount, transaction_date
FROM source_table
WHERE year = 2023 AND month = 2;

--Querying Partitioned Tables:
SELECT *
FROM sales1
WHERE year = 2023 AND month = 1;
--------------------------------------------------
--Creating a Bucketed Table:
CREATE TABLE bucketed_sales (
    transaction_id INT,
    amount DECIMAL(10, 2),
    transaction_date STRING
)
CLUSTERED BY (transaction_id) INTO 4 BUCKETS;

--Loading Data into Bucketed Tables:
LOAD DATA INPATH 'hdfs://path/to/datafile.csv' INTO TABLE bucketed_sales;
--Querying Bucketed Tables for Improved Performance:
SELECT *
FROM bucketed_sales s
JOIN customers c ON s.transaction_id = c.customer_id;
