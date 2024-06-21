--creating a table
CREATE [MANAGED][EXTERNAL] TABLE foo (id INT);

--default table type can be set at database level.
CREATE DATABASE test_db WITH DBPROPERTIES ('defaultTableType'='EXTERNAL');

/*You can also choose to configure a database to allow only external tables to be 
created and prevent creation of ACID tables
*/
CREATE DATABASE test_db WITH DBPROPERTIES('EXTERNAL_TABLES_ONLY'='true');

--Set the default table type at a session level
hive.create.as.external.legacy to true or false --When the session ends, the default CREATE TABLE behavior also ends.

--Set the default table type at a site level
hive.create.as.insert.only and hive.create.as.acid --properties  in Cloudera Manager


