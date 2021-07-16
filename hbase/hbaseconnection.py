import json 
import os

import uuid
import requests
from requests.models import Response
from requests_kerberos import HTTPKerberosAuth , OPTIONAL


# pqs_server = 'http://sandbox-hdp.hortonworks.com:8765/'
# pqs_server = 'http://sandbox-hdp.hortonworks.com:8765/;serialization=JSON'
pqs_server = 'http://172.18.0.2:8765/;serialization=JSON'
pqs_server = 'http://192.168.191.130:8765/;serialization=JSON'
# pqs_server = 'http://sandbox-hdp.hortonworks.com:8765/;serialization=JSON'


def openConnection(connId):
    headers = {"request" :"{'request':'openConnection', 'connectionId': '"+connId+"'}"}
    print(headers)
    return headers


def closeConnection(connId):
    headers = {"request" :"{'request':'closConnection', 'connectionId': '"+connId+"'}"}
    print(headers)
    return headers

def createStatement(connId):
    headers = {"request" :"{'request':'createStatement', 'connectionId': '"+connId+"'}"}
    print(headers)
    return headers

def prepareRequest(connId, data):
    headers = {'request' : '{"request": "prepare", "connectionId": "'+connId+'", "sql":"'+data+'"}'}
    print(headers)
    return headers

def commit(connId):
    headers = {"request" : "{'request' :'commit', 'connectionId': '"+connId+"'}"}
    print(headers)
    return headers


def prepareAndExecuteRequest(connId, stmtId, sqlStr):
    headers = {'request': '{"request" : "prepareAndExecute", "connectionId": "'+connId+'", "statementId": '+stmtId+', "sql": "'+sqlStr+'"}'}
    print(headers)
    return headers

def closeStatement(connId, stmtId):
    headers = {"request": "{'request': 'closeStatement', 'connectionId': '"+connId+"', 'statementId': '"+stmtId+"' }"}
    print(headers)
    return headers

def executeBatchRequest(connId, stmtId, values):
    headers = {'request' : '{"request": "executeBatch", "connectionId": "'+connId+'", "statementId": '+stmtId+',"parameterValues": [['+values+']]}'}
    print(headers)
    return headers


def post(url, headers):
    try:
        # with kerberos auth
        # os.environ['KRB5CCNAME'] = '/tmp/krb5cc_***'
        # import subprocess
        # subprocess.run(["klist"])
        session = requests.Session()
        session.auth = HTTPKerberosAuth(mutual_authentication=OPTIONAL)
        response = session.post(url, headers=headers)
        print("passing in headers")
        print(headers)
        assert response.status_code == 200, "something went wrong with POST requests  " + str(response.status_code)
        return response.text
    except AssertionError as ae:
        raise RuntimeError(ae)


# def parseResponse(responseString, searchKey):
#     try: 
#         response_Json= json.loads(responseString)
#     except Exception as e:
#         raise Exception(e)
#     else:
#         if searchKey in response_Json.keys():
#             response_Json[searchKey]
#         else:
#             raise KeyError(searchKey + "NOT int the resonpse")

# # def parseResult(response):
# #     try:
#         json_string = json.loads(response)
#         list_cols = []
#         list_rows = []
#         tl_dict = []

#         for result in json_string['results']:
#             for key in result['signature']['columns']:
#                 list_cols.append(str(key['columnName']).lower())
#             if result['firstFrame']['done'] == True:
#                 row_size = len(json_string[])


def getResponse():
    sql_str = "select * from us_population"
    connection_id  = str(uuid.uuid1())
    # print(connection_id)
    connection_header = openConnection(connection_id)
    
    connection_response_text = post(pqs_server, connection_header)
    print("="*100)
    connection_header
    # statement_header = createStatement(connection_id)
    # statement_response_text = post(pqs_server, statement_header)
    # print()
    # print(statement_response_text)


getResponse()

