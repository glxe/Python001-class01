from selenium import webdriver
import time
import requests


# 石墨登录

try:
    browser = webdriver.Chrome()

    browser.get('https://shimo.im/welcome')
    time.sleep(2)
    browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('15888888888')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('sfds')
    time.sleep(2)
    loginBtn = browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')
    loginBtn.click()

    cookies = browser.get_cookies()
    print(cookies)
    
except Exception as e:
    pass
finally:
    print('end')
    browser.close()
