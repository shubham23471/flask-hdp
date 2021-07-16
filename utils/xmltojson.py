#!/home/datamaking/softwares/anaconda3/envs/flaskde/bin/python

# This script is used in NIFI to convert the xml data to json  

from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import json
import os


def xmltojson(xml_file_nm, temp_file_nm):
    with open(xml_file_nm, "r") as input_file:
        jsonOut = bf.data(fromstring(input_file.read()))
        # print(type(jsonOut))
        # only storing sms data
        # print(jsonOut['smses']['sms'])
        with open(temp_file_nm, "w+") as newFile:
            json.dump(jsonOut['smses']['sms'], newFile, ensure_ascii=False)


def get_sms_data(temp_file_nm, sms_file_name):

    with open(temp_file_nm, 'r') as input_file:
        lines = input_file.readlines()
    # open new file
    with open(sms_file_name, 'w+') as out_file:
        for line in lines:
            if '@' in line:
                out_file.write(line.replace('@', ''))
                # print(line.replace('@', ''))
            else:
                out_file.write(line)
                # print(line)


if __name__ == "__main__":
    
    # name = 'sms-20210307001157'
    xml_file_nm = '/home/datamaking/projects/flask_pipeline/flask_app/inout/xml/sms-20210307001157.xml'
    # just the formated conversion from xml to json 
    temp_file_nm = '/home/datamaking/projects/flask_pipeline/flask_app/inout/json/temp_file.json'
    
    # final json data from removing special charachter
    # for now keeping the final json file name as  file_name.xml
    sms_file_name = '/home/datamaking/projects/flask_pipeline/flask_app/inout/json/sms-20210307001157.json'
    xmltojson(xml_file_nm, temp_file_nm)
    get_sms_data(temp_file_nm, sms_file_name)
    os.remove(temp_file_nm)
