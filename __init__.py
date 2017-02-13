from selenium import webdriver

chrome_path = "C:\chromedriver.exe"
web = webdriver.Chrome(chrome_path)
web.maximize_window()
web.get('http://prod.tibame.net')