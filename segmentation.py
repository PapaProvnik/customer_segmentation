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

#Trying to find number of clusters using Elbow Method
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(df[['Age', 'Family_Size']])
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

#Gives an elbow method according to Age and fam size. Clearly breaks off at 2.
#Source: https://www.kaggle.com/code/mikecoronagonzalez/lab-5-k-means-clustering

def a_f():

    #This is segment by clarifying 3 clusters by age and family size.
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(df[['Age', 'Family_Size']])

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='Family_Size',
    hue='Cluster', palette='viridis')
    plt.title('Customer Segments')
    plt.show()

    features = ['Age', 'Family_Size']  # Adjust based on your dataset
    X = df[features]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # based on elbow method
    optimal_k = 4  # Change this based on the Elbow Method graph

    # 6. Applying K-Means with chosen K
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Visualizing clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['Age'], y=df['Family_Size'], hue=df['Cluster'], palette='viridis', s=100)
    plt.title(f'K-Means Clustering (K={optimal_k})')
    plt.xlabel('Age')
    plt.ylabel('Family Size')
    plt.legend(title='Cluster')
    plt.show()

def a_em():
    pass

def a_f_w_ss(): #DO NOT USE - ABSOLUTE ASS
    features = ['Age', 'Family_Size', 'Work_Experience', 'Spending_Score_Average', 'Spending_Score_High', 'Spending_Score_Low']
    X = df[features]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X) 

    inertia = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()

    optimal_k = 4  # Update based on the new Elbow Method graph
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    sns.pairplot(df, hue='Cluster', palette='viridis')
    plt.title(f'K-Means Clustering (K={optimal_k})')
    plt.show()

a_f()