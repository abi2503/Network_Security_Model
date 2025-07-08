import os,sys
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS
from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.exception import NetworkSecurityException
from networksecurity.entity.artifact_entity import DataValidationArtifact,DataTransformationArtifact

from networksecurity.entity.config_entity import DataTransformationConfig #This goes as input for data_transformation cpmponent
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import save_object,save_numpy_array_data


class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig,
                 data_validation_artifact:DataValidationArtifact):
        try:
            self.data_transformation_config=data_transformation_config
            self.data_validation_artifact=data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    

    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info("Entered the initiate_data_transformation method of DataTransformation class")

            train_df=pd.read_csv(self.data_validation_artifact.valid_train_file_path)
            test_df=pd.read_csv(self.data_validation_artifact.valid_test_file_path)

            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN]
            target_feature_train_df=target_feature_train_df.replace(-1,0)

            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df=test_df[TARGET_COLUMN]
            target_feature_test_df=target_feature_test_df.replace(-1,0)
            logging.info("Applying preprocessing object on training and testing datasets")

            preprocessor=self.get_data_transformer_object()
            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature=preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature=preprocessor_object.transform(input_feature_test_df)
            #np.c_ is used to concatenate the transformed input train feature and target feature train array as numpy arrays
            train_arr=np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr=np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]

            save_numpy_array_data(file_path=self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array_data(file_path=self.data_transformation_config.transformed_test_file_path,array=test_arr)
            #Creates a pickle file for the preprocessor object
            save_object(file_path=self.data_transformation_config.preprocessor_object_file_path,obj=preprocessor_object)
            #Preparing the artifact
            data_transformation_artifact=DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_config.preprocessor_object_file_path
            )
            logging.info(f"Data transformation artifact: {data_transformation_artifact}")
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def get_data_transformer_object(self)->Pipeline:
        logging.info("Entered the get_data_transformer_object method of DataTransformation class")
        try:
            imputer:KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initiated KNNImputer with parameters: {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            processor:Pipeline=Pipeline([("imputer",imputer)])
            return processor


        except Exception as e:  
            raise NetworkSecurityException(e,sys)





