from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

@dataclass
class DataValidationArtifact:
    report_file_path:str   # we are writing str as we are saying that it stores the string value

class DataTransformationArtifact:...
class ModelTrainerArtifact:...
class ModelEvaluationArtifact:...
class ModelPusherArtifact:...