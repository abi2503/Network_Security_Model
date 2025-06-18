from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logging
from networksecurity.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
import numpy as np

#Configuration of data ingestion configuration

from networksecurity.entity.config_entity import DataIngestionConfig

import os
import sys
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.db=self.mongo_client[self.data_ingestion_config.database_name]
            self.collection_name=self.data_ingestion_config.collection_name
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def export_collection_as_dataframe(self,collection_name:str,database_name:str):
        """
        Export entire collection as a pandas dataframe
        """
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]#This is used to get the collection from the database
            df=pd.DataFrame(list(collection.find()))#This is used to convert the collection to a dataframe
            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)#This is used to drop the _id column from the dataframe
            df.replace({"na":np.nan},inplace=True)#This is used to replace the na values with nan
            return df
        except Exception as e:
            raise NetworkSecurityException(e,sys)
  
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
            dataframe = self.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name,
                database_name=self.data_ingestion_config.database_name
            )
            logging.info("Got the data from mongodb")
            
            # Create feature store directory
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_file_path), exist_ok=True)
            logging.info(f"Exporting collection to {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            
            # Create train-test split
            train_df, test_df = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Exported collection data as csv file")
            
            # Create directories for train and test files
            train_file_path = self.data_ingestion_config.training_file_path
            test_file_path = self.data_ingestion_config.test_file_path
            os.makedirs(os.path.dirname(train_file_path), exist_ok=True)
            os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
            
            logging.info(f"Exporting train dataset to file: [{train_file_path}]")
            train_df.to_csv(train_file_path, index=False, header=True)
            logging.info(f"Exporting test dataset to file: [{test_file_path}]")
            test_df.to_csv(test_file_path, index=False, header=True)
            logging.info("Exported train and test dataset")
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=train_file_path,
                test_file_path=test_file_path
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    def export_data_into_feature_store(self):
        """
        Export mongodb collection record as pandas dataframe into feature store folder
        """
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        """
        Split data as train test
        """
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio,random_state=42)
            logging.info(f"Splitting data into train and test")
            logging.info(f"Exited split_data_as_train_test method of Data_Ingestion class")
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
