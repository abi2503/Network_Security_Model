from networksecurity.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception import NetworkSecurityException
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from scipy.stats import ks_2samp#Checks 2 samples of data to detect data drift
import pandas as pd
import os,sys

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.schema_config=self.read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
        



