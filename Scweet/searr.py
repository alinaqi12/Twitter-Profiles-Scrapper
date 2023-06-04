from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


userr1 = 'imran'
path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'

browser = webdriver.Chrome(path)

browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')

i = 1
for i in range(20):

    print('searching')
    try:
        w  = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span')))
        print(w.text)
    except Exception as e:
        print(e)
    
    time.sleep(5)
browser.quit()
browser.close()