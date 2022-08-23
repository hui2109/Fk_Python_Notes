from selenium import webdriver
import time

browser = webdriver.Firefox(executable_path='./geckodriver')
time.sleep(3)
browser.get('https://www.crazyit.org/')
time.sleep(5)
