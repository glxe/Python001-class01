import requests

# #GET 请求

# r = requests.get('https://www.baidu.com')
# r.status_code
# r.text
# print(r.json)

# # POST 请求

# r = requests.post('https://httpbin.org/post')

# print(r.json())


# 在同一个Session实例发出的所有请求之间保持cookie
# s = requests.session()

# s.get('https://httpbin.org/cookies/set/aaa/4444')

# r = s.get('https://httpbin.org/cookies')

# print(r.json())
# https://httpbin.org/cookies/set/aaa/4444

# 也可以使用上下文管理器
with requests.session() as s:
    a = s.get('https://httpbin.org/cookies/set/aaa/4444')
    print(a.json())





  
# from selenium import webdriver

# import time

# try:
#     browser = webdriver.Chrome()
#     # 需要安装chrome driver, 和浏览器版本保持一致
#     # http://chromedriver.storage.googleapis.com/index.html
    
#     browser.get('https://www.douban.com')
#     time.sleep(1)

#     browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
#     btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
#     btm1.click()

#     browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
#     browser.find_element_by_id('password').send_keys('test123test456')
#     time.sleep(1)
#     browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

#     cookies = browser.get_cookies() # 获取cookies
#     print(cookies)
#     time.sleep(3)

# except Exception as e:
#     print(e)
# finally:    
#     browser.close()