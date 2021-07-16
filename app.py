from flask import Flask, request, Response, session, jsonify
from utils.apperrors import errors
from utils.config import *
import logging
import socket
import sys
from logging import handlers
from waitress import serve
from hive.hiveconnect import HiveOperations

# print("{}.{}".format(schema_mapping["dev"], output_tables["final_data_tbl"]))

app = Flask(__name__)
app.register_blueprint(errors)
app.secret_key = "SMSAPP"


logger = logging.getLogger("SMS_LOGS")
logger.setLevel(logging.DEBUG)
watched_hdlr = logging.handlers.WatchedFileHandler("logs/SMSAPP.log")
LOGGER_FORMAT = (
    "%(asctime)s %(levelname)s %(filename)s:%(lineno)s - %(funcName)20s() %(message)s"
)
formatter = logging.Formatter(LOGGER_FORMAT)
watched_hdlr.setFormatter(formatter)
logger.addHandler(watched_hdlr)


@app.route("/", methods=["GET", "POST"])
def printHello():
    return "Hello World!!"


@app.route("/sms", methods=["GET", "POST"])
def runApp():
    # assert schema_env in schema_mapping.keys(), schema_env + "is not a valida schema!!!"

    return {"msg": "inside runApp"}


if __name__ == "__main__":
    try:
        host = socket.gethostname()
        port = 6969
        schema_env = sys.argv[1]
        hive = HiveOperations(host, user, pwd)

        assert schema_env in schema_mapping.keys(), (
            schema_env + " is not a valid running env!!!"
        )
        app.run(host=host, port=port)
    except RuntimeError as e:
        logger.debug(e)


# error with below
# - not able to see the output on the terminal after hosting with waitress

# if __name__ == "__main__":
#     try:
#         host = socket.gethostname()
#         port=6969
#         # , host='0.0.0.0'
#         print(host)
#         schema_env = sys.argv[1]
#         assert schema_env in schema_mapping.keys(), schema_env + " is not a valid running env!!!"
#         print('1')
#         if(host):
#             print('2')
#             # serve(app, host='0.0.0.0', port=6969, threads=2)
#             serve(app, host=host, port=port, threads=2)
#             print("Starting app: {host}.{port}".format(host=host, port=port))
#         else:
#             raise Exception("Unable to find the hostname")
#     except RuntimeError as e:
#         logger.debug(e)
