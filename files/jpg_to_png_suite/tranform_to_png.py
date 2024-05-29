import PIL.ExifTags
from PIL import Image


def trans_PNG(initial_pic, new_pic):
    '''
    to get a transparent picture
    :param initial_pic: initial picture's path
    :param new_pic: the transparent picture's path
    :return:
    '''
    img = Image.open(initial_pic)

    # 将白色及近似白色的地方改成半透明
    datas = img.getdata()
    new_data = list()
    for item in datas:
        # print(item)
        # if item[0] == 0:
            # print(111)
        if item[0] > 160 and item[1] > 160 and item[2] > 160:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    img.putdata(new_data)
    img.save(new_pic, "PNG")


if __name__ == '__main__':
    # trans_PNG('../test_images/2021.png', "./2021.png")
    # trans_PNG('../test_images/5.png', "./5.png")
    # trans_PNG('../test_images/13.png', "./13.png")
    trans_PNG(r'2024.png', r"2024_bak.png")
