import json
from cookie_get import get_c

# 将字典保存到文档
def save_dict_to_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print("字典已成功保存到文档。")
    except Exception as e:
        print(f"保存字典失败：{e}")

# 从文档中读取字典
def load_dict_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"读取字典失败：{e}")
        return None

if __name__ == "__main__":
    domainName = "kuaishou.com"
    type_c = "chrome"
    dict_cookie = get_c(domainName, type_c)
    print(dict_cookie)
    my_dict = isinstance(dict_cookie, dict)
    # 要保存的字典数据
    # dict_cookie = {'name': 'Alice', 'age': 30, 'city': 'New York'}

    # 将字典保存到文档
    file_path = './datas/data.json'
    save_dict_to_file(dict_cookie, file_path)

    # 从文档中读取字典
    loaded_dict = load_dict_from_file(file_path)
    if loaded_dict:
        print("从文档中读取的字典数据：")
        print(loaded_dict)
