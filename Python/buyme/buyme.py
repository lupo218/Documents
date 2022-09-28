from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
driver.get('https://buyme.co.il/?modal=login')
# time.sleep(10)
driver.find_element(By.XPATH, '//input[@id=\'ember1769\']').send_keys("xx@xx.com") #הזדהות
driver.find_element(By.XPATH, '//input[@id=\'ember1776\']').send_keys("xxx")
driver.find_element(By.XPATH,'//*[@id="ember1785"]').click()

time.sleep(1) # עמוד ראשי
driver.find_element(By.XPATH,'//*[@id="ember1049"]/div/div[1]').click() # בחירה
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember1073"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember1084"]/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember1107"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember1116"]/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember1172"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember1195"]').click()
time.sleep(1)# בחירה 2
driver.find_element(By.XPATH,'//*[@id="ember2025"]/div[2]').click()
time.sleep(1) # הכנס סכום
driver.find_element(By.XPATH,'//*[@id="ember2256"]').send_keys("200")
driver.find_element(By.XPATH,'//*[@id="ember2262"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember2384"]').click() # עמוד למי לשלוח
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember2388"]').send_keys("דורון")

driver.find_element(By.XPATH,'//*[@id="ember2399"]/textarea').send_keys("בהצלחה עם המחזור 1803")
driver.find_element(By.ID,'ember2408').send_keys('C:\\Users\\lupo2\\Pictures\\IMG-20210908-WA0034.jpg') # העלת קובץ
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember2449"]/div/div[1]').click() # בחירת אירוע
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember2487"]').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[3]/div[2]/button').click()
time.sleep(1) # איך לשלוח
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/div/div/div[1]/form/div[4]/div[2]/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="sms"]').send_keys("0508195442")
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="ember2579"]').send_keys("0508195442")
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/form/div[4]/div[2]/button').click()# סיום
time.sleep(1)