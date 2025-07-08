from dataclasses import dataclass
"""
The dataclass is a decorator that automatically adds special methods to the class, such as __init__(), __repr__(), and __eq__()
The dataclass is used to create a class that is used to store the data of the artifact.
"""
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

@dataclass#This class keeps track of the output schema of the data validation stage
class DataValidationArtifact:
    validation_status:bool
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str
    transformed_train_file_path:str
    transformed_test_file_path:str

