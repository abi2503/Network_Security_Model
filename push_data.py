##This file collects raw data from the csv file and pushes it to the mongo db client as json format
import os
import sys
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging import logger
import pandas as pd
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import certifi #Importing certifi to avoid SSL errors and check trusted certificates while via https or tls connections
import pandas as pd
import numpy as np
import pymongo
import json

ca = certifi.where()#This is used to get the path to the trusted certificates
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class NetworkDataExtract:#This class is used to extract data from the csv file and convert it to json format
    def __init__(self):
        try:
            pass
        except:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json(self,csv_file_path:str):
        try:
            df = pd.read_csv(csv_file_path)
            df.reset_index(drop=True,inplace=True)
            records=list(json.loads(df.T.to_json()).values())#This is used to convert the dataframe to list of json arraysjsons
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.records=records
            self.database=database
            self.collection=collection
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[database]
            self.collection=self.database[collection]
            self.collection.insert_many(records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__=="__main__":
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE="Network_Security_Data_Repository"
    COLLECTION="phishing_data"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json(csv_file_path=FILE_PATH)
    number_of_records=networkobj.insert_data_to_mongodb(records,DATABASE,COLLECTION)


    print(records)
    print(number_of_records)
    
        
        
        