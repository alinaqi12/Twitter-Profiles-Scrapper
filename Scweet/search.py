from Scweet.scweet import scrape
import undetected_chromedriver as uc
from Scweet.user import get_user_information, get_users_following, get_users_followers
import Scweet.user
env_path = ".env"
import csv
import pandas
import time

from Scweet import utils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import selenium
from time import sleep
import random
import json
import csv


user = 'imran khan'
driver = uc.Chrome(use_subprocess = True )
driver.get(f"https://twitter.com/search?q={user}&src=typed_query&f=user")
list_of_users_get = []
for i in range(1,50):
    try: 
        q = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span')))
        print(q.text)
        list_of_users_get.append(q.text)
    except Exception as e: 
        print(e)

print(len(list_of_users_get))