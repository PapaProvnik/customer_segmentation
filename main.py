import pandas as pd
import os
import json

from data_loaders import truncate_table

with open("db_credentials.json", "r") as file:
    cred = json.load(file)

DB_USER = cred["db_user"]
DB_PASSWORD = cred["db_password"]
DB_HOST = cred["db_host"]
DB_NAME = cred["db_name"]

DATA = "customer_segmentation_data"

