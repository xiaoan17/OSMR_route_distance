import requests

# 设置OSRM服务器的URL
osrm_server_url = "http://router.project-osrm.org"

# 定义起点和终点的经度、纬度
start_coords = "-117.032486,32.544463"
end_coords = "-117.061845,32.558459"

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
    print(f"Distance: {distance} meters")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
