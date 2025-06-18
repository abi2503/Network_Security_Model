import os
import sys
import numpy as np
import pandas as pd

"""
Defining common constant variables for training pipeline
"""

TARGET_COLUMN:str="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="phisingData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"
SCHEMA_FILE_PATH:str=os.path.join("networksecurity","data_schema","schema.yaml")

"""
Defining common constant variables for training pipeline
"""

TRAINING_PIPELINE_CONFIG_KEY:str="training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY:str="artifact_dir"
TRAINING_PIPELINE_NAME_KEY:str="pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR:str="artifact"

"""
Data validation related constant start with DATA_VALIDATION_*
"""
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.yaml"
DATA_VALIDATION_REPORT_FILE_NAME:str="report.yaml"

"""
Data ingestion related constant start with DATA_INGESTION_*
"""

DATA_INGESTION_COLLECTION_NAME:str="phishing_data"
DATA_INGESTION_DATABASE_NAME:str="Network_Security_Data_Repository"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2

"""
Data transformation related constant start with DATA_TRANSFORMATION_*
"""

DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"