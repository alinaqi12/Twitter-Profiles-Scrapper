import time
import os
import requests
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
import pyautogui
import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
def get_user_information( driver=None, headless=True):
    """ get user information if the "from_account" argument is specified """

    driver = utils.init_driver(headless=False)
    users = ["@ImranKhanPTI"]
    users_info = {}

    for i, user in enumerate(users):
        flag = 0

        log_user_page(user, driver)

        if user is not None:
            pyautogui.keyDown("ctrl")
            pyautogui.press("r")
            pyautogui.keyUp("ctrl")
            try: 
                followww  = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
            except Exception as e:
                print("Account is protected")
                flag =1
                continue
            try:
               # time.sleep(3)
                follo = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
                #follo = driver.find_element(By.XPATH,'//a[contains(@href,"/following")]/span[1]/span[1]')
                #following = driver.find_element_by_xpath(
                    #'//a[contains(@href,"/following")]/span[1]/span[1]').text
                following = follo.text
                #follo = driver.find_element(By.XPATH, '//a[contains(@href,"/followers")]/span[1]/span[1]')
                followers = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,'//a[contains(@href,"/followers")]/span[1]/span[1]'))).text
                #followers = driver.find_element_by_xpath(
                    #'//a[contains(@href,"/followers")]/span[1]/span[1]').text
                #followers = follo.text
            except Exception as e:
                print("------------")
                if flag == 0:
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("r")
                    pyautogui.keyUp("ctrl")
                # print(e)
                #following=""
                #followers=""
                #print(e)

            try:
                element = driver.find_element_by_xpath('//div[contains(@data-testid,"UserProfileHeader_Items")]//a[1]')
                website = element.get_attribute("href")
            except Exception as e:
                # print(e)
                website = ""

            try:
                desc = driver.find_element_by_xpath('//div[contains(@data-testid,"UserDescription")]').text
            except Exception as e:
                # print(e)
                desc = ""
            a = 0
            try:
                join_date = driver.find_element_by_xpath(
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[3]').text
                birthday = driver.find_element_by_xpath(
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
                location = driver.find_element_by_xpath(
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
            except Exception as e:
                # print(e)
                try:
                    join_date = driver.find_element_by_xpath(
                        '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[2]').text
                    span1 = driver.find_element_by_xpath(
                        '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
                    if hasNumbers(span1):
                        birthday = span1
                        location = ""
                    else:
                        location = span1
                        birthday = ""
                except Exception as e:
                    # print(e)
                    try:
                        join_date = driver.find_element_by_xpath(
                            '//div[contains(@data-testid,"UserProfileHeader_Items")]/span[1]').text
                        birthday = ""
                        location = ""
                    except Exception as e:
                        # print(e)
                        join_date = ""
                        birthday = ""
                        location = ""
            try:
                tweetno = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").text
                print(tweetno)
            except Exception as e:
                print("Not found")
            try:
                print("--------------- " + user + " information : ---------------")
                print("Following : ", following)
                print("Followers : ", followers)
                print("Location : ", location)
                print("Join date : ", join_date)
                print("Birth date : ", birthday)
                print("Description : ", desc)
                print("Website : ", website)
                users_info[user] = [following, followers, join_date, birthday, location, website, desc]
                Profiles_header = ['name', 'following', 'followers', 'location','join_date','birthday','bio','website']
                Profiles_data = [ user , following , followers , location, join_date, birthday, desc, website, ]
            except Exception as e:
                print(e)
                pyautogui.keyDown("ctrl")
                pyautogui.press("r")
                pyautogui.keyUp("ctrl")
            try: 
                # Creating list to append tweet data to
                tweets_list1 = []

                # Using TwitterSearchScraper to scrape data and append tweets to list
                for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()):
                    if i>150:
                        break
                    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
                    
                # Creating a dataframe from the tweets list above 
                tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
                tweets_df1.to_csv(f'Tweets/{user}.csv', sep=',', index=False)

                                #os.system(f"snscrape --format '{content!r}' --max-results 100 twitter-search 'from:{user}'> {user}-tweets.json")
            except Exception as e:
                print("--------")
            with open('Profiles/Profiles.csv', 'a', encoding='utf') as file:
                writer = csv.writer(file)
                #writer.writerow(Profiles_header)
                writer.writerow(Profiles_data)
            if i == len(users) - 1:
                driver.close()
                driver.quit()
                return users_info
            try:
                #driver1 = uc.Chrome(use_subprocess = True )
                #driver1.get(f"https://twitter.com/{user}/photo")
                #time.sleep(3)
                #driver1.save_screenshot(f"D:\FYP\Scweet-master\yo\{user}.png")
                #time.sleep(1)
                #driver1.quit()
                #driver1.close()
                URL = f"https://unavatar.io/twitter/{user}"
                response = requests.get(URL)
                # 3. Open the response into a new file 
                open(f"images/{user}-profilepic.png", "wb").write(response.content)
                URL2 = f"https://twitter.com/{user}/header_photo"
                response = requests.get(URL2)
                # 3. Open the response into a new file 
                open(f"images/{user}-coverpic.png", "wb").write(response.content)
                
            
            except Exception as e:
                print("-------------------")
        else:
            print("You must specify the user")
            continue
        sleep(2)


def log_user_page(user, driver, headless=True):
    sleep(random.uniform(1, 2))
    driver.get('https://twitter.com/' + user)
    sleep(random.uniform(1, 2))


def get_users_followers(users, env, verbose=1, headless=True, wait=2, limit=float('inf'), file_path=None):
    followers = utils.get_users_follow(users, headless, env, "followers", verbose, wait=wait, limit=limit)

    if file_path == None:
        file_path = 'outputs/' + str(users[0]) + '_' + str(users[-1]) + '_' + 'followers.json'
    else:
        file_path = file_path + str(users[0]) + '_' + str(users[-1]) + '_' + 'followers.json'
    with open(file_path, 'w') as f:
        json.dump(followers, f)
        print(f"file saved in {file_path}")
    return followers


def get_users_following(users, env, verbose=1, headless=True, wait=2, limit=float('inf'), file_path=None):
    following = utils.get_users_follow(users, headless, env, "following", verbose, wait=wait, limit=limit)

    if file_path == None:
        file_path = 'outputs/' + str(users[0]) + '_' + str(users[-1]) + '_' + 'following.json'
    else:
        file_path = file_path + str(users[0]) + '_' + str(users[-1]) + '_' + 'following.json'
    with open(file_path, 'w') as f:
        json.dump(following, f)
        print(f"file saved in {file_path}")
    return following


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def search(user):
    driver.get(f"https://twitter.com/search?q={user}&src=typed_query&f=user")
    list_of_users_get = []
    for i in range(1,28):
        q = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span')))
        print(q.text)
get_user_information()