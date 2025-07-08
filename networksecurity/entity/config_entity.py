from datetime import datetime
import os
from networksecurity.constant import training_pipeline
from networksecurity.exception import NetworkSecurityException
import sys

class TrainingPipelineConfig:#This class is used to store the configuration for the training pipeline
    def __init__(self,timestamp=datetime.now()):
        timestamp=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp=timestamp

class DataIngestionConfig:#This class is used to store the configuration for the data ingestion pipeline
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.database_name:str=training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name:str=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.data_ingestion_dir:str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
        self.training_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME)
        self.test_file_path:str=os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME)
        self.train_test_split_ratio:float=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir:str=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path:str=os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str=os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str=os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str=os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str=os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)

class DataTransformationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir:str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_dir:str=os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_NAME)
        self.transformed_test_dir:str=os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_NAME)
        self.transformed_train_file_path:str=os.path.join(self.transformed_train_dir,"train.npy")
        self.transformed_test_file_path:str=os.path.join(self.transformed_test_dir,"test.npy")
        self.preprocessor_object_file_path:str=os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,"preprocessor.pkl")
        



print(training_pipeline.DATA_INGESTION_COLLECTION_NAME)
print(training_pipeline.DATA_INGESTION_DIR_NAME)
print(training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
print(training_pipeline.DATA_INGESTION_INGESTED_DIR)
print(training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION)
print(training_pipeline.DATA_INGESTION_DATABASE_NAME)
print(training_pipeline.TARGET_COLUMN)
print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

