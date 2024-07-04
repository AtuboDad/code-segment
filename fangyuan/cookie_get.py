import browser_cookie3
# import pyperclip as pc

def get_c(domainName,type_c):
    chrome_list = ["chrome","谷歌浏览器","谷歌"]
    firefox_list = ["firefox","火狐浏览器","火狐"]
    try:
        if type_c in chrome_list:
            dict1 = browser_cookie3.chrome(domain_name=domainName)
        elif type_c in firefox_list:
            dict1 = browser_cookie3.firefox(domain_name=domainName)
        else:
            dict1 = browser_cookie3.chrome(domain_name=domainName)
            pass
        dict_cookie = {}
        for u in dict1:
            # s = (u.name + ": " + u.value )
            dict_cookie[u.name] = u.value
            # print(s)
            # pc.copy(s)
            # cc = pc.paste()
            # print(cc)
        return dict_cookie
    except Exception as get_e:
        return get_e








