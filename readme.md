# URLs

1. (NIFI)[http://localhost:8080/nifi/]
2. Beeline : beeline -u jdbc:hive2://
3. Hiveserver2: http://localhost:10002/
    hiveserver2 &
4. HBASE: 
    - Go to /home/datamaking/softwares/hbase-2.2.6-bin/hbase-2.2.6/bin and then run start-hbase.sh 
    - HBASE LOGS: /home/datamaking/softwares/hbase-2.2.6-bin/hbase-2.2.6/logs
                    21124 NameNode
                    900 QuorumPeerMain
                    23382 HMaster
                    21338 DataNode
                    21594 SecondaryNameNode
                    23546 HRegionServer
                    23995 Jps
                    908 Kafka
                    22028 NodeManager
                    21839 ResourceManager
5. To start and stop docker. Stop: sudo service docker stop.
6. To see if any of the service is running: sudo systemctl status zookeeper
7. HBASE: 
    - https://stackoverflow.com/questions/40223422/hbase-master-wont-start



# Things to learn
1. How to insert data into hive using pyhive. 
2. Run spark-submit job. 
3. Multi-threding in python 




# APP TODO
(functions for )
1. [x] Insert JSON to HDFS.
2. [x] Convert json into csv from app and then save it into hive table. 
3. [] Sending EMAIL in python and in bash script. 
4. [x] Use of 'tempfile' while running the spark-submit.
5. [] HASE Connection using Python.
6. [] Setup kerberos and then execute everything.
7. [x] Multi-threding in app. 
8. [] work with jsonparser. 




# Hosting 
- using waitress rn 