import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException


# if we have a collection we can use find function to call all the data in the collection
def get_collection_as_dataframe(database_name:str,collection_name:str)-> pd.DataFrame:
    '''
    Description : This function returns collection as dataframe
    ==================================================================
    Params:
    database_name: database name
    collection_name : collection name
    ==================================================================
    return Pandas Dataframe of a collection
    '''
    try:
        logging.info(f"Reading data from database:{database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns : {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: '_id'")
            df = df.drop("_id",axis = 1)
        logging.info(f"Row and Columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)