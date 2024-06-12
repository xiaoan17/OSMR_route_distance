import pandas as pd
import numpy as np
from geopy.distance import geodesic

# 读取CSV文件
file_path = 'sd_meta.csv'
data = pd.read_csv(file_path)

# 提取经纬度信息
locations = data[['Lat', 'Lng']].values

# 获取检测器数量
num_detectors = len(locations)

# 初始化邻接矩阵
adj_matrix = np.zeros((num_detectors, num_detectors))

# 计算距离并构建邻接矩阵
for i in range(num_detectors):
    for j in range(num_detectors):
        if i == j:
            continue
        dist = geodesic(locations[i], locations[j]).m
        if dist <= 4000:
            adj_matrix[i, j] = dist
            adj_matrix[j, i] = dist

# 保存邻接矩阵到npy文件
output_path = 'Lat_Lon_adj_matrix.npy'
np.save(output_path, adj_matrix)
