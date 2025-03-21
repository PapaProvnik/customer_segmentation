import pandas as pd
import os
import json
import numpy as np

from data_loaders import truncate_table, upload_df_to_sql
import segmentation

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

            #filling in NULL values
            df_test['Age'].fillna(df_test['Age'].mean(), inplace=True)
            df_test['Work_Experience'].fillna(df_test['Work_Experience'].mean(), inplace=True)
            df_test['Family_Size'].fillna(df_test['Family_Size'].mean(), inplace=True)

            # Mode imputation for categorical columns
            df_test['Gender'].fillna(df_test['Gender'].mode()[0], inplace=True)
            df_test['Ever_Married'].fillna(df_test['Ever_Married'].mode()[0], inplace=True)
            df_test['Graduated'].fillna(df_test['Graduated'].mode()[0], inplace=True)
            df_test['Profession'].fillna(df_test['Profession'].mode()[0], inplace=True)
            df_test['Var_1'].fillna(df_test['Var_1'].mode()[0], inplace=True)

            #rounding replaced values
            df_test["Family_Size"] = np.ceil(df_test["Family_Size"])

            df_test.to_csv(os.path.join(DATA, "df_test_no_nulls.csv"))

            #Mapping numerical values to text fields
            df_test["Gender"] = df_test["Gender"].map({"Male" : 0, "Female" : 1})
            df_test["Ever_Married"] = df_test["Ever_Married"].map({"No" : 0, "Yes" : 1})
            df_test["Graduated"] = df_test["Graduated"].map({"No" : 0, "Yes" : 1})
            df_test = pd.get_dummies(df_test, columns=["Profession", "Spending_Score"], dtype=int)

            print(df_test.head())
            df_test.to_csv(os.path.join(DATA, "df_test_normalised.csv"))

def customer_segmentation(df):
    pass

data_normalisation()