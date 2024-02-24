# -*- coding: utf-8 -*-
"""customer seg kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18NKbhuhdsgSV6HVlDeP0hy0Aqnr4ThtM
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

customer_data = pd.read_csv("/content/Mall_Customers.csv")

customer_data.head()

customer_data.shape

customer_data.info()

customer_data.isnull().sum()

x = customer_data.iloc[:,[3,4]].values

print(x)

wcss = []

for i in range(1,11):
  kmeans = KMeans(n_clusters=i,init = "k-means++" ,random_state=42)
  kmeans.fit(x)

  wcss.append(kmeans.inertia_)

sns.set()
plt.plot(range(1,11),wcss)
plt.title("The flow point graph")
plt.xlabel("The number of clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=5,init="k-means++",random_state = 0)

y = kmeans.fit_predict(x)

print(y)

plt.figure(figsize=(8,8))
plt.scatter(x[y==0,0], x[y==0,1], s=50, c='green', label='Cluster 1')
plt.scatter(x[y==1,0], x[y==1,1], s=50, c='red', label='Cluster 2')
plt.scatter(x[y==2,0], x[y==2,1], s=50, c='yellow', label='Cluster 3')
plt.scatter(x[y==3,0], x[y==3,1], s=50, c='violet', label='Cluster 4')
plt.scatter(x[y==4,0], x[y==4,1], s=50, c='blue', label='Cluster 5')


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')

plt.title('Customer Groups')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.show()