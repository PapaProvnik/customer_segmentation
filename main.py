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
    pass

def customer_segmentation(df):
    pass

