from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#1
def firefox01(url):
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\lupo2\Downloads\\geckodriver-v0.30.0-win64\\geckodriver.exe')
    driver.get(url)
firefox01('https://www.walla.co.il/')


def chrome01(url):
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get(url)

#chrome01('https://ynet.co.il')

#2
def chrome_title(url,title):
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    time.sleep(2)
    driver.refresh()
    print(title == driver.title)

#chrome_title(url,'ynet - חדשות, כלכלה, ספורט ובריאות - דיווחים שוטפים מהארץ ומהעולם')

#3
# Yes

# 4 & 6
def translate(word):
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get('https://translate.google.com')
    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys(word)
    #driver.find_element(By.CLASS_NAME, 'er8xn').send_keys(word)
    #driver.find_element(By.TAG_NAME, 'textarea').send_keys(word)
    time.sleep(1)
    resulte = (driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span')).text
    print(f'The translation to {word} is:{resulte}')
    print(driver.find_element(By.CLASS_NAME, 'er8xn'))

#translate('גיא')

#5

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

#7
def facebook():
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.facebook.com/')
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("aa@aa.aa")
    driver.find_element(By.XPATH, '// *[ @ id = "pass"]').send_keys("bla bla")
    time.sleep(20)

#facebook()

#8
def cookies():
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.facebook.com/')
    print(driver.get_cookies())
    driver.delete_all_cookies()
    if len(driver.get_cookies()) == 0:
        print('All all cookies was delete')
    else:
        print('Error')

#cookies()

#9

def github():
    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe')
    driver.get('https://github.com/')
    elemen = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
    elemen.send_keys('Selenium')
    elemen.send_keys(Keys.ENTER)
    time.sleep(20)

#github()

#10
def chrome_disable_extensions():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(executable_path='G:\chromedriver_win32\chromedriver.exe',chrome_options=options)
    driver.get('https://github.com/')
    elemen = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
    elemen.send_keys('Selenium')
    elemen.send_keys(Keys.ENTER)
    time.sleep(20)


#chrome_disable_extensions()



