from subprocess import PIPE, Popen
import os


env_variables = os.environ.copy()
env_variables["HADOOP_CONF_DIR"] = "/home/datamaking/softwares/hadoop-3.2.1/etc/hadoop"

run_pyspark = Popen(
    [
        "spark-submit",
        "--master",
        "yarn",
        "--num-executors",
        "2",
        "--driver-memory",
        "2g",
        "--executor-memory",
        "1g",
        "--executor-cores",
        "2",
        "/home/datamaking/projects/flask_pipeline/flask_app/pyspark/test_pyspark.py",
    ],
    stdout=PIPE,
    stderr=PIPE,
    env=env_variables,
)

print("Running pyspark script with pid: {}".format(run_pyspark.pid))
(output, error) = run_pyspark.communicate()
print(
    "=====================Return code from the process : {}========================".format(
        run_pyspark.returncode
    )
)
print(output, error)
