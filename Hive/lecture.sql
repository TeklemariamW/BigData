sudo -u hdfs hdfs dfs -chmod 777 /tmp/catbd125/uttam/emp/
create table loaddatam(id int, name string) row format delimited fields terminated by ',' stored as textfile; 
LOAD DATA INPATH '/tmp/catbd125/uttam/emp/emp2.csv' INTO TABLE loaddatam;
insert into loaddatam1 select * from loaddatam;
 create table loaddatam2 as select * from loaddatam;

 create table loaddatam3 like loaddatam; --copy a metadata only

 

