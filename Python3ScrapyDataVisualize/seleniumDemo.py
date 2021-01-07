# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#利用selenium进行爬虫
import requests
import urllib
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def get_url(url):
  time.sleep(5)
  return requests.get(url)
def get_routes(xpath,numbers):
  results = driver.find_elements_by_xpath(xpath)
  print(len(results))
  if(len(results )> numbers):
      print("toute1111",len(results))
      return results
  #实现窗口滑动
  #driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  #ActionChains(driver).key_down(Keys.DOWN).perform()
  ac=driver.find_element_by_css_selector('#app > div > main > div.loadmore');
  ActionChains(driver).move_to_element(ac).perform()#定位鼠标到指定元素
  time.sleep(5)
  return get_routes(xpath, numbers)

      
if __name__ == "__main__":
  path = "/usr/local/bin/chromedriver"
  driver = webdriver.Chrome(executable_path=path)
  dept_cities = ["北京","上海","成都","广州","深圳"]
  for dep in dept_cities:
    strhtml = get_url('https://dujia.qunar.com/golfz/sight/arriveRecommend?dep='+urllib.request.quote(dep)+'&extensionImg=255,175')
    arrive_dict = strhtml.json()
    for arr_item in arrive_dict['data']:
      for arr_item1 in arr_item['subModules']:
        for query in arr_item1['items']:
          driver.get('https://fh.dujia.qunar.com/?tf=package')
          #WebDriverWait(driver,10).until(EC.presence_of_element_located(By.ID),'depCity');
          driver.find_element_by_css_selector('#depCity')
          driver.find_element_by_xpath("//*[@id='depCity']").clear()
          driver.find_element_by_xpath("//*[@id='depCity']").send_keys(dep)
          driver.find_element_by_xpath("//*[@id='arrCity']").send_keys(query['query'])
          driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/a").click()
          print("dep:%s arr:%s" % (dep, query['query']))
          time.sleep(10)
          routes = get_routes("/html/body/div/div/main/div[1]/div/div[2]/p[1]/span[1]", 30)
          print("route",routes)
          count = 0
          for route in routes:
              count += 1
              result = {
                  'date':time.strftime('%Y-%m-%d',time.localtime(time.time())),
                  'dep':dep,
                  'arrive':query['query'],
                  'result':route.text
                  }
              print(count,result)                
  driver.close()
  