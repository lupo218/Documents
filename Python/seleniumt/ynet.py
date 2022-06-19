from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def chrome01(url):
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get(url)

chrome01('https://ynet.co.il')