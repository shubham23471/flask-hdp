import socket
import getpass


output_tables = {"raw_data_tbl": "raw_sms", "final_data_tbl": "sms_data"}

schema_mapping = {"dev": "sms_analytics_dev", "prod": "sms_analytics_prod"}

hive_connection = {
    "host": socket.gethostname(),
    # 'user'= getpass.getuser()
}


hdfs_path_dict = {"dev": "/flaskde"}
