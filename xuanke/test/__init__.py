# 输入账号和密码
account = 'xxxxxxxx'
password = 'xxxxxxxx'
# 输入课程名和课程编号
# 如：'信息检索' : '24254.28120030-1.01'
course = {
    'xxxx1': 'xxxxxxxx',
    'xxxx2': 'xxxxxxxx',
}

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
driver = webdriver.Edge()
def begining():
    #打开浏览器
    #访问网站
    driver.maximize_window()
    driver.get('http://jwxt.sias.edu.cn/eams/homeExt.action')
def loading():
    #登录
    driver.find_element(By.ID,'username').send_keys(account)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR,'#loginForm > table > tbody > tr:nth-child(5) > td > input').click()
def JinRu():
    while 1:
        try:
            a = driver.find_element(By.CSS_SELECTOR, "#main-nav > ul > li:nth-child(2) > a")
            ActionChains(driver).move_to_element(a).perform()
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR, '#main-nav > ul > li:nth-child(2) > ul > li:nth-child(7) > a').click()
        except:
            pass
        else:
            break
def JinRu2():
    time.sleep(0.5)
    driver.switch_to.frame("iframeMain")
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[3]/a").click()
    driver.switch_to.default_content()
begining()
loading()
JinRu()
JinRu2()
v="//*[@id='electableLessonList']/thead/tr[1]/th[2]/div/input"
course={
'信息检索' : '24254.28120030-1.01'
}
time.sleep(3)
handles = driver.window_handles
driver.switch_to.window(handles[-1])
while 1:
            for key in course:
                try:
                    driver.find_element(By.XPATH, v).click()
                    driver.find_element(By.XPATH, v).send_keys(Keys.CONTROL, 'a')
                    driver.find_element(By.XPATH, v).send_keys(Keys.BACKSPACE)
                    driver.find_element(By.XPATH, v).send_keys(course[key])
                    driver.find_element(By.XPATH, v).send_keys(Keys.ENTER)
                    time.sleep(1)
                    driver.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[1]/table/tbody/tr/td[16]/a').click()
                    # 弹窗
                    cf = driver.switch_to.alert
                    cf.accept()
                    time.sleep(1)
                    driver.find_element(By.CSS_SELECTOR, '#cboxClose').click()
                    l1 = driver.find_element(By.CSS_SELECTOR, '#cboxClose')

                except:
                        continue
                else:
                        break
