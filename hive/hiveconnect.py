## T0D0
## Fucntion for
## 1. put_hdfs: load data from csv to hdfs location
## 2. create_stage table : creat staging table for  csv
## 3. load_stage_table : Load csv data to stage table
## 4. load_final_table : load datad from stage table to final table

from pyhive import hive
import logging
from logging import handlers


logger = logging.getLogger("SMSAPP")

print("here1")


class HiveOperations:
    AUTH_TYPE = "LDAP"
    ATTEMPTS = 0

    def __init__(self, host, user, pwd):
        self.host = host
        self.user = user
        self.pwd = pwd
        # os.environ["SASL_PATH"] = "/usr/lib64/sasl2"
        print("here")
        self.connection = hive.connect(
            host=self.host, auth=self.AUTH_TYPE, username=self.user, password=self.pwd
        )

    def close_connection(self):
        logger.info("CLOSSING CONNECTIONS..")
        self.connection.close()

    def run_stmt(self, stmt):
        try:
            logger.info("Running HQL stmt")
            cursor = self.connection.cursor()
            cursor.execute(stmt)
            cursor.close()
        except Exception as e:
            logger.debug("Got Exception while running HQL statement %s" % e)

    def get_records(self, stmt):
        try:
            logger.info("Getting records from table")
            df = pd.read_sql(stmt, self.connection)
            return df
        except Exception as e:
            logger.debug("Got Exception while fetching record from hive %s" % e)


# you can use run_stmt Fucntion to create seprate functions to create_stage_tbl, load_stage_table , load_final_table
# for create table use : create table if not exists db.stage_table row format delimeted fields terminated by "," stored as text file
#                        tblproperties('seralization.null.format'='') as select * from db.another_table where 1=2

# for load table use : load data inpath hdfs_path overwrite into table db.stage_table
# load into final table : insert into db.final_table from db.stage_table
