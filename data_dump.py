import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
DATABASE_COLLECTION = "sensor"

if __name__ == "__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape}")

# convert the records to json formt to load on mongDB

df.reset_index(drop = True ,inplace = True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])

#insert converted json records to mangoDB as only json format are uploaded on mongoDB

client[DATABASE_NAME][DATABASE_COLLECTION].insert_many(json_record)