# -*- coding: utf-8 -*-

import pandas as pd
import time
import random


def login_douban():
    """
    功能：使用playwright自动登录豆瓣
    """
    # 进入登录页面
    login_url = 'https://accounts.douban.com/passport/login?source=movie'
    page.goto(login_url)
    time.sleep(2)

    # 点击密码登录
    page.click('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]')
    time.sleep(2)
    # 输入账号和密码
    page.type('//*[@id="username"]', '13625962371', delay=150)
    time.sleep(2)
    page.type('//*[@id="password"]', 'woxihuanni1314', delay=150)

    time.sleep(3)
    # 点击登录
    page.click('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a')
    time.sleep(20)


def get_douban_comment(movie_id):
    # 总表
    df_all = pd.DataFrame()

    for page_num in range(11, 13):
        # 获取URL
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(movie_id, page_num * 20)

        # 打印进度
        print('正在获取第{}页的信息'.format(page_num + 1))

        # 发起请求
        page.goto(url)

        # 休眠一秒
        time.sleep(random.randint(2, 5))

        user_infos = page.querySelectorAll('div.comment-item span.comment-info a')
        # 获取用户名
        user_name = [user_info.innerText() for user_info in user_infos]
        # 获取主页URL
        page_url = [user_info.getAttribute('href') for user_info in user_infos]
        # 获取评分
        rating_num = [i.getAttribute('title') for i in page.querySelectorAll('div.comment-item span.comment-info span:nth-child(3)')]
        # 获取评论时间
        comment_time = [i.getAttribute('title') for i in page.querySelectorAll('div.comment-item span.comment-info span:nth-child(4)')]
        # 短评信息
        short_comment = [i.innerText() for i in page.querySelectorAll('div.comment-item span.short')]
        print('user_name', user_name)

        # 存储数据
        df_one = pd.DataFrame({
            'user_name': user_name,
            'page_url': page_url,
            'rating_num': rating_num,
            'comment_time': comment_time,
            'short_comment': short_comment
        })
        print(df_one)
        df_one.to_csv("./douban_data/zhuangtai{}.csv".format(page_num))
        # 追加
        df_all = df_all.append(df_one, ignore_index=True)

    print('爬虫程式结束，共获取数据{df_all.shape[0]}条')
    browser.close()
    playwright.stop()

    return df_all


# 先登录豆瓣
login_douban()
df = get_douban_comment(movie_id='30458950')
