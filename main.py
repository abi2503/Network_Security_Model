from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig
import sys
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformation

if __name__=="__main__":
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info(f"Data ingestion started")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed")
        
        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation=DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        logging.info(f"Data validation started")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info(f"Data validation completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transformation=DataTransformation(data_transformation_config=data_transformation_config,data_validation_artifact=data_validation_artifact)
        logging.info(f"Data transformation started")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info(f"Data transformation completed")
        print(data_transformation_artifact)

    except Exception as e:
        print(e)
        logging.exception(e)
        raise NetworkSecurityException(e,sys)

