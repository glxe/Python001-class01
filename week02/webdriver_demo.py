from selenium import webdriver
import time
import requests

# 豆瓣登录
# try:
#     browser = webdriver.Chrome()

#     browser.get('https://douban.com')
#     time.sleep(1)

#     browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
#     btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
#     btm1.click()

#     browser.find_element_by_xpath('//*[@id="username"]').send_keys('15370383786')
#     browser.find_element_by_xpath('//*[@id="password"]').send_keys('funcid79325')
#     time.sleep(1)
#     loginBtn = browser.find_element_by_xpath('//a[@class="btn btn-account btn-active"]')
#     loginBtn.click()

#     cookies = browser.get_cookies()
#     print(cookies)
    
#     # ///html/body/div[1]/div[2]/div[1]/div[5]/a
# except Exception as e:
#     pass
# finally:
#     print('end')

# 石墨登录

# try:
#     browser = webdriver.Chrome()

#     browser.get('https://shimo.im/welcome')
#     time.sleep(2)
#     browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
#     time.sleep(3)
#     browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('15370383786')
#     browser.find_element_by_xpath('//input[@name="password"]').send_keys('funcid79325')
#     time.sleep(2)
#     loginBtn = browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')
#     loginBtn.click()

#     cookies = browser.get_cookies()
#     print(cookies)
    
# except Exception as e:
#     pass
# finally:
#     print('end')
#     browser.close()




#file download
# imageRrl = 'https://img1.doubanio.com/view/photo/l/public/p624842928.webp'
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
# r = requests.get(imageRrl, headers = headers) # 一开始没加headers 然后http status code 是418([418的梗](https://www.zhihu.com/question/41318710/answer/90500171))。加了headers就正常了
# print(r.content)
# with open('p624842928.webp', 'wb') as f:
#     f.write(r.content)


###  大文件下载
#  如果文件比较大的话，那么下载下来先放在内存中，内存还是有很大的压力的
# 所以为了防止内存被消耗完，我们需要想办法把下载的文件分块写到磁盘中

fileUrl = "https://v3-tt.ixigua.com/24e0d689616c1bb6a2a330a3004425e3/5efb6afd/video/tos/cn/tos-cn-vd-0026/8c2711bab29540b5a11b2d48303b7029/media-video-avc1/?a=1768&br=5856&bt=1952&cr=0&cs=0&dr=0&ds=3&er=0&l=202006302335560100140440810439D94E&lr=default&mime_type=video_mp4&qs=2&rc=Mzc2cjlrcG08dDMzZzczM0ApZTQ4ZmY6NDxnN2ZlPDtlZWcxLWteYy5zZWdfLS0xLS9zc2A2MC82NWIxYS8yNmBjXjA6Yw%3D%3D&vl=&vr="
fileName = "8c2711bab29540b5a11b2d48303b7029.mp4";
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
r = requests.get(fileUrl, headers = headers, stream = True) # 一开始没加headers 然后http status code 是418([418的梗](https://www.zhihu.com/question/41318710/answer/90500171))。加了headers就正常了
# print(r.content)

with open(fileName, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            f.write(chunk)