from time import sleep
import time

from selenium import webdriver

from Auto.Login import *


class OpenDriver():
    
    def __init__(self,x):
        
        self.x = x
        
    def open(self):

        global web
        chrome_path = "C:\chromedriver.exe"
        web = webdriver.Chrome(chrome_path)
        web.maximize_window()
        web.get('http://prod.tibame.net')

    def loginStep(self):
        
        user = Login(None)
        choice = user.input()
        userId = [user.User(choice)]
        
        loginBtn = web.find_element_by_xpath("//*[@id='content']/div/nav/div/div[2]/ul[2]/li[3]/a/button")
        loginBtn.click()
        
        time.sleep(3)
        
        if choice == 0 or choice == 1:
            
            keyUserId = web.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/form/div/div[3]/input")
            keyUserPw = web.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/form/div/div[4]/input")
        
            keyUserId.send_keys(userId[0][0])
            keyUserPw.send_keys(userId[0][1])
        
            time.sleep(2)
        
            loginBtn2 = web.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[2]/form/div/div[6]/button")
            loginBtn2.click()
            
        if choice == 2:
            
#             keyUserId = web.find_element_by_xpath("//*[@id='identifier-shown']")
#             keyUserId.send_keys(userId[2][0])
            
            print  "google"
        if choice == 3:
            print  "facebook"
      
        
        