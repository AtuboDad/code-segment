import requests
 
# 链接地址
url = 'https://minedbuildings.blob.core.windows.net/global-buildings/buildings-coverage.geojson'
 
# 发送GET请求
response = requests.get(url)
 
# 检查请求是否成功
if response.status_code == 200:
    # 获取内容
    content = response.content
    
    # 打开文件进行二进制写入
    with open('buildings-coverage.geojson', 'wb') as file:
        file.write(content)
else:
    print('Failed to retrieve the webpage')