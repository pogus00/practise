from sklearn.cluster import KMeans
import numpy as np

# 用戶輸入數據點數量
n_points = int(input("Please enter the number of data points: "))

# 定義一個空數據集
data = []

# 逐個輸入數據點 (x, y)
for i in range(n_points):
    x = float(input(f"Enter x-coordinate of point {i+1}: "))
    y = float(input(f"Enter y-coordinate of point {i+1}: "))
    data.append([x, y])

# 將數據轉換為 numpy array 格式
data = np.array(data)

# 用戶輸入 K 值 (即幾多個簇)
k = int(input("Please enter the number of clusters (K): "))

# 初始化 KMeans 演算法
kmeans = KMeans(n_clusters=k)

# 訓練 KMeans 模型
kmeans.fit(data)

# 獲取每個數據點所屬的簇
labels = kmeans.labels_

# 獲取每個簇的中心點
centroids = kmeans.cluster_centers_

# 輸出結果
print("\nK-means clustering result:")
for i, label in enumerate(labels):
    print(f"Point {i+1} with coordinates {data[i]} is in cluster {label+1}")

print("\nCentroids of each cluster:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")
