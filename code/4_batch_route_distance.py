import numpy as np
import requests
import time


def calculate_distance(start_coords, end_coords):
    # 设置OSRM服务器的URL
    osrm_server_url = "http://router.project-osrm.org"

    # 构建URL以调用OSRM的route服务
    route_url = f"{osrm_server_url}/route/v1/driving/{start_coords};{end_coords}"

    # 定义参数
    params = {
        "overview": "false",  # 可以是 "simplified" 或 "full" 或 "false"
        "geometries": "polyline"  # 结果中的几何形状格式
    }

    # 发送GET请求
    response = requests.get(route_url, params=params)

    # 检查响应状态
    if response.status_code == 200:
        # 解析响应内容
        route_data = response.json()
        # 提取距离信息（以米为单位）
        distance = route_data['routes'][0]['distance']
        return distance
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


task_info = np.load('tasks_list.npy')

# 定义每批次的请求数量和暂停时间
batch_size = 512
pause_time = 0.01

count = 0

# 找到 task_info[:, -1] 为 NaN 或者 0 的所有索引
condition = np.isnan(task_info[:, -1]) | (task_info[:, -1] == 0)
nan_zero_index = np.where(condition)[0]
print(f"Task start from {nan_zero_index} -- total task == {len(nan_zero_index)}")

for index in nan_zero_index:
    start_coords = f"{task_info[index][2]},{task_info[index][3]}"
    end_coords = f"{task_info[index][4]},{task_info[index][5]}"
    result = calculate_distance(start_coords, end_coords)
    task_info[index][-1] = result
    # 打印显示进度
    count += 1
    print(f"Task {index} completed == {count} == {result} meters")
    # 暂停一段时间以避免过多的请求
    if count % batch_size == 0:
        time.sleep(pause_time)

    # 每经过100个任务，保存一次结果
    if count % 100 == 0:
        np.save('tasks_list.npy', task_info)
        print("Progress saved")

np.save('tasks_list.npy', task_info)
print("Progress saved")
