/*
External table drop: Hive drops only the metadata, consisting mainly of the schema.
Managed table drop: Hive deletes the data and the metadata stored in the Hive warehouse.
*/

--start Hive
hive
--Create a CRUD transactional table named T having two integer columns, a and b
CREATE TABLE T(a int, b int);
--Confirm that you created a managed, ACID table
DESCRIBE FORMATTED T;

---Creating an insert-only transactional table
/***
 In the CREATE TABLE statement, specifying a storage type other than ORC, 
 such as text, CSV, AVRO, or JSON, results in an insert-only ACID table.
**/
CREATE TABLE T2(a int, b int) 
  STORED AS ORC
  TBLPROPERTIES ('transactional'='true',
  'transactional_properties'='insert_only');

--or
CREATE TABLE T3(a int, b int) 
STORED AS TEXTFILE;

-----Creating, using, and dropping an external table
1. -- Create a text file named students.csv that contains the following lines.
--1,jane,doe,senior,mathematics 2,john,smith,junior,engineering
2. --Move the file to HDFS in a directory called andrena, and put students.csv in the directory.
3. --Start the Hive shell.
4. --Create an external table schema definition that specifies the text format, loads data from students.csv in /user/andrena.
id,firstname,lastname,country,phonenumber
CREATE EXTERNAL TABLE IF NOT EXISTS students( 
id INT,
firstname STRING, 
lastname STRING, 
country STRING, 
phonenumber INT) 
COMMENT 'Student Names' 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE LOCATION '/tmp/catbd125/Tekle/hivql/data2';

--Verify that the Hive warehouse stores the student names in the external table.
select * from students;

--Create the schema for a managed table
CREATE TABLE IF NOT EXISTS Names(
student_ID INT, 
FirstName STRING, 
LastName STRING, 
year STRING, 
Major STRING) 
COMMENT 'Student Names';

--Move the external table data to the managed table.
INSERT OVERWRITE TABLE Names SELECT * FROM names_text;

/*
Verify that the data from the external table resides in the managed table, 
and drop the external table, and verify that the data still resides in the managed table
*/
SELECT * from Names; DROP TABLE studentT; SELECT * from Names;

--Verify that the external table schema definition is lost.
SELECT * from studentT;
----------------------------------------------------------------------
---create external table insert data using 'load data inpath...'
CREATE EXTERNAL TABLE IF NOT EXISTS external_test_data (
    user_id STRING,
    user_name STRING,
    user_email STRING,
    registration_date DATE
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
--Location: /tmp/catbd125/Tekle/hivql/studentT.csv
--hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/warehouse/tablespace/external/hive/external_test_data
LOAD DATA INPATH 'hdfs://ip-172-31-3-80.eu-west-2.compute.internal:8020/tmp/catbd125/Tekle/hivql/studentT.csv' INTO TABLE external_test_data;
LOAD DATA INPATH '/tmp/catbd125/Tekle/hivql/studentT.csv' INTO TABLE external_test_data;
--Change permission
sudo -u hdfs  hdfs dfs -chmod -R 777  /warehouse/tablespace/external/hive/external_test_data