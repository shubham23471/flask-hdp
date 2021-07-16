# from hive.hiveconnect import HiveOperations
# import socket
# import getpass

# host = socket.gethostname()
# user = getpass.getuser()
# pwd = " "
# print(host, user)


# hive = HiveOperations(host, user, pwd)
# print(hive)

# stmt = "select * from datamaking_db.customer"
# stmt = "insert into datamaking_db.customer values(3, 'shakya', 'Delhi')"
# df = hive.run_stmt(stmt)
# print(stmt)


###############################################################################
########################---- Hadoop put ---- ##################################
###############################################################################

# import os
# from hadoop.hadoop import HadoopOperations
# from utils.config import hdfs_path_dict

# csv_path = "/inout/csv/"
# project_path = os.getcwd()
# load_file_path = project_path + csv_path
# # print(load_file_path)
# file_name = os.listdir(load_file_path)[0]
# # print(os.listdir(load_file_path)[0])

# hadoop = HadoopOperations()
# # print(hadoop)
# # print(load_file_path + file_name)
# file_path = load_file_path + file_name

# hadoop.put_hdfs(file_path, hdfs_path_dict["dev"])

# # load_file_path = "/home/datamaking/projects/flask_pipeline/flask_app/inout/csv/sms-20210307001157.csv"


###############################################################################
########################---- Running spark submit ---- ########################
###############################################################################

# from subprocess import PIPE, Popen
# import tempfile
# import os

# temp_file = tempfile.NamedTemporaryFile()
# temp_file_id = temp_file.fileno()

# env_variables = os.environ.copy()
# # export HADOOP_CONF_DIR=/home/datamaking/softwares/hadoop-3.2.1/etc/hadoop
# env_variables["HADOOP_CONF_DIR"] = "/home/datamaking/softwares/hadoop-3.2.1/etc/hadoop"


# try:
#     # EXECUTING: spark-submit --master yarn --num-executors 2 --driver-memory 2g --executor-memory 2g --executor-cores 2
#     run_pyspark = Popen(
#         [
#             "spark-submit",
#             "--master",
#             "yarn",
#             "--num-executors",
#             "2",
#             "--driver-memory",
#             "2g",
#             "--executor-memory",
#             "1g",
#             "--executor-cores",
#             "2",
#             "/home/datamaking/projects/flask_pipeline/flask_app/pyspark/test_pyspark.py",
#         ],
#         stdout=temp_file_id,
#         env=env_variables,
#     )

#     from re import findall, sub

#     # change Print to logger for later use
#     print("Running pyspark script with pid: {}".format(run_pyspark.pid))
#     (output, error) = run_pyspark.communicate()
#     print(
#         "=====================Return code from the process : {}========================".format(
#             run_pyspark.returncode
#         )
#     )
#     print(output, error)
#     print()
#     with open(temp_file.name) as f:
#         matches = findall(r"Exception:(.*)", str(f.readlines()))
#         f.close()

#     matches = sub('\[|\]|;|\'|`|\\\|u"|"', "", str(matches))
#     print("matches =", matches)

#     if run_pyspark.returncode < 0:
#         print("Spark script failed with code: {}".format(run_pyspark.returncode))
#     elif run_pyspark.returncode == 0:
#         print("Spark script ran succesfuly")
#     else:
#         print(
#             "Script got gfailed with error => Return code: {} \n Error: {}".format(
#                 run_pyspark.returncode, matches
#             )
#         )

# except ProcessLookupError as pe:
#     raise Exception(matches)


###############################################################################
########################---- Multi-Threading ---- #############################
###############################################################################
#### Idea is to wait for futher execution intil all the ingestion of data got completed
####

from concurrent.futures import ThreadPoolExecutor, wait
from collections import OrderedDict
import time


def func1(msg):
    print("inside func1")
    return msg


def func2(msg):
    # time.sleep(4)
    x
    print("inside func2")
    return msg


threads_args = ["Hello", "Shubham"]


def thredPool(targets, args):
    """
    target: functions which you want to execute
    args : argument for these functions
    """
    try:
        num_of_threads = 2
        args = args * len(targets)
        # print(args)
        arg_list = OrderedDict()
        arg_list = dict(
            zip(targets, args)
        )  # {<function func1 at 0x7f3927433950>: 'Hello', <function func2 at 0x7f3927446dd0>: 'Shubham'}
        # print(arg_list)
        # print([arg_list])
        pool = ThreadPoolExecutor(num_of_threads)

        futures = []
        futures_res = []

        for fn in list(arg_list):
            futures.append(pool.submit(fn, arg_list[fn]))

        complete, incomplete = wait(futures, return_when="ALL_COMPLETED")
        print(complete, incomplete)

        for idx, x in enumerate(futures):
            print(idx, x, x._exception)
            if x._exception:
                print(
                    str(list(arg_list)[idx])
                    + " failed with exception "
                    + str(x._exception)
                )
            elif x._state == "FINISHED":
                futures_res.append(x._result)
        return futures_res
    except Exception as e:
        raise Exception(e)


running_threads = thredPool([func1, func2], threads_args)
