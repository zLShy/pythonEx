#coding=utf-8
from selenium import webdriver
import time
chromedrive = "/Users/zhangli/Downloads/chromedriver"
browser = webdriver.Chrome(chromedrive)
browser.get("http://www.baidu.com")
# # browser.find_element_by_id("kw").send_keys("selenium")
# # browser.find_element_by_id("su").click()
# browser.implicitly_wait(10)
# print browser.title
# # browser.set_window_size(480,960)
# browser.maximize_window()
# time.sleep(3)
# second_url='http://news.baidu.com'
# browser.get(second_url)
# time.sleep(3)
# browser.get("http://www.baidu.com")
# time.sleep(3)
# browser.quit()

browser.find_element_by_id("kw").clear();
browser.find_element_by_id("kw").send_keys(u"图片")
browser.find_element_by_id("su").submit()
time.sleep(5)
browser.quit()
