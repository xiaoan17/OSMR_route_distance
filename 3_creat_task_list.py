import numpy as np
import pandas as pd

# 假设你有一个存储部分节点距离信息的npy文件
adj_matrix = np.load('Lat_Lon_adj_matrix.npy')

# ID,Lat,Lng,District,County,Fwy,Lanes,Type,Direction,ID2
sd_meta = pd.read_csv("sd_meta.csv")
sd_meta = np.array(sd_meta)

# 提取邻接矩阵中距离大于0的元素，创建任务列表
tasks = []
for i in range(adj_matrix.shape[0]):
    for j in range(adj_matrix.shape[1]):
        if adj_matrix[i, j] > 0:
            temp = [i, j, sd_meta[i][2], sd_meta[i][1], sd_meta[j][2], sd_meta[j][1], adj_matrix[i, j], 0]
            tasks.append(temp)

tasks = np.array(tasks)
# 保存邻接矩阵到npy文件
output_path = 'tasks_list.npy'
np.save(output_path, tasks)
