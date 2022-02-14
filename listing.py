import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from akru_login import Login
from config import TestData


def listing():
   driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
   driver.maximize_window()
   driver.implicitly_wait(10)
   driver.get(TestData.AKRU)
   window_before = driver.current_window_handle

   """CALLING LOGIN FUNCTION"""
   loginn = Login(driver)
   loginn.login() 
   time.sleep(4)

   """LISTING LINK"""
   driver.find_element(By.LINK_TEXT,'Listings').click()  

   """CLICK ON PROPERTY"""
   property = driver.find_element(By.ID,'property6206054a758cffb28ca6a2ac').click()
   # = driver.find_element(By.XPATH,'//*[@id="property6206054a758cffb28ca6a2ac"]/div[1]/div[2]/span')

#    if property == goal_reached:
#        property.click()
#        print("list")
   driver.find_element(By.ID,'singleProperty-secondary-invest').click()
   time.sleep(10)
   balance = driver.find_element(By.XPATH,'//*[@id="isBuy"]/div/div[1]/div[2]/span[1]/span')
   usd = balance.get_attribute("textContent")
   a = float(str(usd))
   print(a)
   amount= int(float(usd))
   print(usd)
   print(amount)

   if amount >= 1000.00:
       print(usd)
       
   time.sleep(20)

listing()       