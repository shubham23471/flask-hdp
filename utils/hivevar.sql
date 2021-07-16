set hivevar:TABLE_NAME=TEST_DB;
set hivevar:START_DATE='2016-01-01';

SELECT ${TABLE_NAME};
select ${START_DATE};
select 

create table if not exists testingdb.test
id int ,
name string
stored as ORC TBLPROPERTITES ('ORC.COMPRESS'='SNAPPY')