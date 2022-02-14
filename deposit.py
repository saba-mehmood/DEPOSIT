
from ast import Assert
from faulthandler import is_enabled
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
from akru_login import Login
from alerts import Alerts
from yopmail import Yopmail
from config import TestData

"""LOCATORS"""
deposit_button =(By.XPATH,'//*[@id="root"]/div/div[3]/section[2]/div/div/div[2]/section/div/div/div/div[1]/div/div/form/div[2]/button')


def deposit():
   driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
   driver.maximize_window()
   driver.implicitly_wait(10)
   driver.get(TestData.AKRU)
   window_before = driver.current_window_handle

   """CALLING LOGIN FUNCTION"""
   loginn = Login(driver)
   loginn.login() 

   time.sleep(4)
   driver.find_element(By.ID,'toWallet').click()
   time.sleep(8)
   #driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section[2]/div/div/div[1]/div[2]/div/span').click()

   """ADD BANK"""
   try:
    driver.find_element(By.NAME,'routingNo').send_keys("021000021")
    driver.find_element(By.NAME,'accountNo').send_keys("18124")
    driver.find_element(By.NAME,'confirmAccountNo').send_keys("18124")
    driver.find_element(By.NAME,'bankName').send_keys("sara")
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section[2]/div/div/div[2]/section/div/div/div/div[2]/div/div/form/button').click()
    time.sleep(1)
   

    """HANDLE ALERT"""
    a = Alerts(driver)
    a.alert_error()
    time.sleep(15)

    driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section[2]/div/div/div[2]/section/div/div/div/div[3]/div[1]/div/div/span[1]/a').click()
    time.sleep(2)

    driver.find_element(By.NAME,'amount1').send_keys('0.01')
    driver.find_element(By.NAME,'amount2').send_keys('0.01')
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div[3]/button').click()
    time.sleep(1)

    """HANDLE ALERT"""
    a = Alerts(driver)
    a.alert_error()
    time.sleep(15)
   
   except NoSuchElementException:
      print(".")


   """DEPOSIT AMOUNT"""
   driver.find_element(By.NAME,'amount').send_keys("25000")
   deposit_btn = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section[2]/div/div/div[2]/section/div/div/div/div[1]/div/div/form/div[2]/button')

   """HANDLING BUTTONS IF DISABLED"""
   if  deposit_btn.is_enabled():
       deposit_btn.click()
   else:
      print("deposit error")
      driver.close()

   """HANDLE ALERT"""
   a = Alerts(driver)
   a.alert_error()
   time.sleep(4)

   """ OTP"""
   driver.execute_script("window.open()")
   driver.switch_to.window(driver.window_handles[2])
   driver.get(TestData.OTP)   
   otp_value= driver.find_element(By.XPATH,'/html/body/pre')

   """USING REGULAR EXPRESSION TO REMOVING TEXT FROM SENTENCE AND GETTING ONLY NUMBERS"""
   value = int(re.sub(r"[^\d.]", "", otp_value.text))  

   """GETTING LAST 4 NUMBERS FROM WHOLE SENTENCE"""
   code=int(str(value)[-4:])
   print("value: %s" % code)
   driver.close()
   
   time.sleep(4)

   """SWICHING BACK TO CONTACT INFO AND ENTER OTP NUMBER"""
   driver.switch_to.window(driver.window_handles[0])
   driver.find_element(By.CLASS_NAME,'code-input').send_keys(code)
   time.sleep(2)
   driver.find_element(By.XPATH,'/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/button[2]').click()

   """HANDLE ALERT"""
   a = Alerts(driver)
   a.alert_error()

   time.sleep(8)
   
  





deposit()    

    

