import requests

url = 'http://localhost:8000/api/slider/files/upload'
files = {"file1": open(r'E:\workspaces\pythonspaces\QT_downloader\simulation\pillow_case\bgPic.jpg', 'rb'),
         "file2": open(r'E:\workspaces\pythonspaces\QT_downloader\simulation\pillow_case\cutPic.png', 'rb')}
response = requests.post(url, files=files)
print(response.text)
