from subprocess import PIPE, Popen
import time
import logging


logger = logging.getLogger("SMSAPP")

# use to load files into HDFS
class HadoopOperations:

    # def __init__(self):

    def put_hdfs(self, local_file_path, hdfs_path):
        try:
            ATTEMPTS = 1
            logger.info("Moving local file to HDFS location")
            put_file = Popen(
                ["hdfs", "dfs", "-put", local_file_path, hdfs_path],
                stdout=PIPE,
                stderr=PIPE,
                bufsize=-1,
            )
            (out, err) = put_file.communicate()
            logger.debug("Subprocess return code: %d" % put_file.returncode)
            logger.debug("put_hdfs command ouput: %s" % out)
            logger.debug("put_hdfs command Error : %s" % out)
            if put_file.returncode != 0:
                time.sleep(3)
                if ATTEMPTS < 3:
                    put_file(local_file_path, hdfs_path)
                else:
                    logger.info("RETRY LIMIT EXCEEDED!")
        except Exception as e:
            raise Exception(e)
