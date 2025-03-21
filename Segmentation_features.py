import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Locating and reading cleansed dataset
DATA = "customer_segmentation_data" # Update this with your actual data folder path
file_path = os.path.join(DATA, "df_test_normalised.csv")
df = pd.read_csv("customer_segmentation_data/df_test_normalised.csv")

# Drop unnecessary columns (ID, names, etc.)
if 'ID' in df.columns:
    df = df.drop(columns=['ID'])

# Check correlation matrix to remove redundant features
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Matrix")
plt.show()

# Standardize numerical features before PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

