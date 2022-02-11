import email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
import time
from config import TestData
from yopmail import Yopmail

#email='avax-35@yopmail.com'
class Login(object):

    def __init__(self,driver):
       self.driver=driver

    def login(self):
      #driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
      #driver.implicitly_wait(10)
     #self.driver.get("https://avaxdev.akru.co/")
      #window_before = self.driver.window_handles[0]
      #driver.execute_script("window.open()")
      self.driver.find_element(By.XPATH,'//*[@id="very-specific-design"]/div/div[2]/div[1]/button[1]').click()
      self.driver.find_element(By.ID,'navbar-header-sticky-login').click()
      self.driver.find_element(By.XPATH,'//*[@id="navbar-header-sticky-login"]/div/div/div/div/button').click()
      self.driver.find_element(By.ID,'navbar-select-magic').click()
      mail = self.driver.find_element(By.ID,'navbar-magic-email').send_keys(TestData.EMAIL)
      self.driver.find_element(By.ID,'navbar-magic-next').click()

      time.sleep(5)

      self.driver.execute_script("window.open()")
      self.driver.switch_to.window(self.driver.window_handles[1])
      self.driver.get("https://yopmail.com/en/")
      self.driver.find_element(By.CLASS_NAME,'ycptinput').send_keys(TestData.EMAIL)
      self.driver.find_element(By.XPATH,'//*[@id="refreshbut"]/button/i').click()
      frame_login = self.driver.switch_to.frame(self.driver.find_element(By.ID,'ifmail'))
      try:
        login_btn=self.driver.find_element(By.XPATH,'//*[@id="mail"]/div/table/tbody/tr/td/div[2]/div/div/div/div/div/div[4]')
        if login_btn.is_displayed() and login_btn.is_enabled():
          login_btn.click()
          
      except:
        login_link=self.driver.find_element(By.LINK_TEXT,'Click here')
        if login_link.is_displayed():
          login_link.click()
      self.driver.close()  
      #driver.switch_to.window(driver.window_handles[1])
      time.sleep(8)
      #driver.switch_to.window(driver.window_handles[0])
      self.driver.switch_to.window(self.driver.window_handles[0])
      time.sleep(4)

      try:
        #switch to alert and print pop up text
       element = WebDriverWait(self.driver, 40).until(
              EC.presence_of_element_located((By.CLASS_NAME, 'Toastify__toast-body'))).get_attribute("textContent")
       print (element)
      except NoAlertPresentException:
        print("exception handled")

      print("Rest of the programm")