import pandas as pd
import os
import json

from data_loaders import truncate_table, upload_df_to_sql

with open("db_credentials.json", "r") as file:
    cred = json.load(file)

DB_USER = cred["db_user"]
DB_PASSWORD = cred["db_password"]
DB_HOST = cred["db_host"]
DB_NAME = cred["db_name"]

DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

DATA = "customer_segmentation_data"

def data_normalisation():
    for file in os.listdir(DATA):
        print(file)
        if "Test" in file:
            file_path = os.path.join(DATA, file)
            df_test = pd.read_csv(file_path)
            print(f"Loaded {file}")

            #Mapping numerical values to text fields
            df_test["Gender"] = df_test["Gender"].map({"Male" : 0, "Female" : 1})
            df_test["Ever_Married"] = df_test["Ever_Married"].map({"No" : 0, "Yes" : 1})
            df_test["Graduated"] = df_test["Graduated"].map({"No" : 0, "Yes" : 1})
            df_test = pd.get_dummies(df_test, columns=["Profession", "Spending_Score"])

            print(df_test.head())
            df_test.to_csv(os.path.join(DATA, "df_test_normalised.csv"))

def customer_segmentation(df):
    pass

data_normalisation()