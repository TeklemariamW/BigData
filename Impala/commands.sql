/*
data lake-----
Medalian Architecture

When you load the data into datalake(Hive is more sutaible)

Bronj---Raw Layer(bring data as it is) mostly with ELT
AI and BI team will explore the data on Bronj Layer.
data discovery it need a lot of query and aggregation to understand the data.(Impala will be hep full)

Silver ---Curated Layer(Tranformation--Spark)
Gold --Application Layer(Data warehouse)---BI Tableau, PowerBI(Connection String from Impala)

When data discovery takes more time beacuse of slow query using hive and imapala,
In that scnario you go with Indexing, Partationing, Bucketing, Query optimization.(performance optimization)
*/
--To delete the metadata saved in the catch
INVALIDATE METADATA