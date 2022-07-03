from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def Youtube():
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.youtube.com/')
    elemen = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    time.sleep(1)
    elemen.send_keys("California Dreamin (Extended Mix)")
    elemen.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]/ytd-thumbnail/a/yt-img-shadow/img').click()
    time.sleep(500)

Youtube()