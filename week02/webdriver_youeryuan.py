from selenium import webdriver
import time
import requests


# 石墨登录
# 王俊斐
# 430104201610060337
# XD140151406
# 长沙市岳麓区中海国际社区中海国际西区四期8栋406房
# 彭小芳
# 18817182016
try:
    browser = webdriver.Chrome()
    browser.get('http://218.76.54.132:8080/signup.html?year=2020&schoolCode=9&env=null&nsukey=HVXvYiI7%2BD8Qxq6Geq2wKrMZCMRkYX0JHy2vSws4xxhNuORoKLcyAeh580kc3T5ZdyNukm%2FoEnUR28SVopqNik2vMWpSj8xc7ZBzjWufOvGXVIGcEkvxvDX%2BwgAm7Gf1bRHf4iT0yx%2BK%2F69uuzTmLgAsapuUIgBYq4g2Zth9kBHpti8ah%2F2%2FrC6IqSquZfFb%2FYYfNcT1Qy%2BqHMbaXQVOZQ%3D%3D')
    time.sleep(2)
    browser.find_element_by_xpath('//input[@name="childName"]').send_keys('王俊斐')
    browser.find_element_by_xpath('//input[@name="childCardNo"]').send_keys('430104201610060337')
    browser.find_element_by_xpath('//input[@name="houseCertiNum"]').send_keys('XD140151406')
    browser.find_element_by_xpath('//input[@name="homeAddr"]').send_keys('长沙市岳麓区中海国际社区中海国际西区四期8栋406房')
    time.sleep(1)
    browser.find_element_by_xpath('//label[@id="slhouseholdAddr"]/div/label[2]').click()
    time.sleep(1)
    browser.find_element_by_xpath('//label[@id="slhouseholdAddr"]/div/ul/li[2]').click()
    time.sleep(1)

    browser.find_element_by_xpath('//input[@name="parentName"]').send_keys('彭小芳')
    browser.find_element_by_xpath('//input[@name="tel1"]').send_keys('18817182016')

    browser.find_element_by_xpath('//a[@class="form-btn s2 btn-s"]').click()
    
except Exception as e:
    pass
finally:
    print('end')
    # browser.close()

