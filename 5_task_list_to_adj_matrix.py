import numpy as np

old_adj_matrix = np.load('Lat_Lon_adj_matrix.npy')

task_info = np.load('tasks_list.npy')

std = np.std(task_info[:, -1])

for i in range(len(task_info)):
    old_adj_matrix[int(task_info[i][0]), int(task_info[i][1])] = np.exp(-task_info[i][-1]**2 / std**2)

np.save('OSMR_adj_matrix.npy', old_adj_matrix)
print('OSMR_adj_matrix.npy saved successfully.')