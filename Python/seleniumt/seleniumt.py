from selenium import webdriver
from  selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


my_driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
my_driver.get('C:\\Users\\lupo2\\Downloads\\tip_calc\\tip_calc\index.html')
my_driver.find_element(By.XPATH, '//*[@id="billamt"]').send_keys("100")
my_driver.find_element(By.XPATH, '//*[@id="peopleamt"]').send_keys("4")
select = Select(my_driver.find_element(By.XPATH, '//*[@id="serviceQual"]'))
select.select_by_value('0.05')
my_driver.find_element(By.XPATH, '//*[@id="calculate"]').click()


tip = my_driver.find_element(By.XPATH, '//*[@id="tip"]')
print(tip.text)
