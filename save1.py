from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options

import time

from socket import socket
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options

import time

options = Options()
options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'  # Path to Firefox binary

options.headless = False


def enter_user(user, depth):
    time1 = 3
    time2 = 5
    path = 'C:\geckodriver.exe'
    depth = depth + 1
    userr1 = user  # input("enter username: ")
    #    browser=utils.init_driver(headless=True)
    browser = webdriver.Firefox(options=options, executable_path=path)

    # browser= webdriver.Firefox(path,options = options)
    print(f"searching against {userr1}")
    browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')

    try:
        browser.get("https://twitter.com/i/flow/login")
        email_xpath = '//input[@autocomplete="username"]'
        password_xpath = '//input[@autocomplete="current-password"]'
        username_xpath = '//input[@data-testid="ocfEnterTextTextInput"]'
        ele = 'nsm7Bb-HzV7m-LgbsSe-MJoBVe'
        username = WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, email_xpath))).click()
        email = "Fyp56D"
        password = "Student@123"
        email_el = browser.find_element(by=By.XPATH, value=email_xpath)
        email_el.send_keys(email)
        email_el.send_keys(Keys.ENTER)

        WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.XPATH, password_xpath)))

        password_el = browser.find_element(by=By.XPATH, value=password_xpath)
        password_el.send_keys(password)
        password_el.send_keys(Keys.ENTER)
        time.sleep(5)
        browser.get(f'https://twitter.com/search?q={userr1}&src=typed_query&f=user')
    except Exception as e:
        print("no need for login")
    for i in range(1, depth):
        try:
            time.sleep(time1)
            # print("========================================")
            follo = WebDriverWait(browser, 100).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div')))
            following = follo.text
        except Exception as e:
            print("oiushfiafhbfaoiahoiahioadfhvoiroiuGADIFOVBI")
            ass = 1
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        with open('new.txt', 'a', encoding="utf-8") as g:
            g.write(following)

    browser.close()
    browser.quit()

    g.close()
   


