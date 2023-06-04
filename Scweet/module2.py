from pickle import FALSE
import time
import pandas as pd
import os
import requests
import json
from Scweet import utils
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from time import sleep
import chromedriver_autoinstaller
import random
import json
import csv 
from csv import DictWriter
import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'

def get_user_information(users ,driver=None, headless=True):
    print(users)
    a=1
    """ get user information if the "from_account" argument is specified """
    try:
        driver = utils.init_driver(headless=True)
        driver.get('https://twitter.com/i/flow/login')
        driver.implicitly_wait(2)
        username = 'mrrobot71598956'
        password = 'Jaguar@1234'
        elementID =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"text")))
        elementID.send_keys(username)
        elementID.send_keys(Keys.ENTER)
        elementID= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
        elementID.send_keys(password)
        elementID.send_keys(Keys.ENTER)
        print('logged in successfully!!')
        sleep(random.uniform(1, 2))
    except Exception as e:
        print('Error in Getting Login Page: ',e)
    
    #----              IF YOU WANT TO TEST THIS CODE ON A SINGLE PROFILE THEN UNCOMMENT THE LINE BELOW     ------
    
    #users = ["@ImranKhanPTI","@elonmusk"]
    users_info = {}

    for i, user in enumerate(users):
        flag = 0

        #log_user_page(user, driver)

        if user is not None:
            print(a, " :---------------: " + user + " information  :---------------:",i)
            try:
                driver.get(f'https://twitter.com/{user}')
            except Exception as e:
                time.sleep(4)
                driver.get(f'https://twitter.com/{user}')    
            try:
                driver.get(f'https://twitter.com/{user}')
            except Exception as e:
                time.sleep(4)
                driver.get(f'https://twitter.com/{user}')
            try:
                driver.get(f'https://twitter.com/{user}')
            except Exception as e:
                time.sleep(4)
                driver.get(f'https://twitter.com/{user}')
            
            time.sleep(1)
            try: 
                followww  = WebDriverWait(driver, 16).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
            except Exception as e:
                print(f"{user}'s Account is protected or doesnot exist")
                flag =1
                continue
            try:
                follo = WebDriverWait(driver, 6).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
                following = follo.text
                followers = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH,'//a[contains(@href,"/followers")]/span[1]/span[1]'))).text
            except Exception as e:
                print("------------")
                if flag == 0:
                    driver.get(f'https://twitter.com/{user}')
                    print("e")
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
                s = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[2]')))
                s1 = s.is_displayed()
                if s1 is False:
                    verification = 0
                else:
                  verification = 1  
                tweetno = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").text
                #tweetno= [int(i) for i in tweetno.split() if i.isdigit()]
                #tweetno = int("".join(tweetno))
                #print(tweetno)
            except Exception as e:
                print("Tweets Not found",e)

            try:
                Full_name = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span').text 
            except Exception as e:
                print ('cannot get name')
            try:
                l = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/nav/div/div[2]/div/div[4]/a')
                driver.execute_script("arguments[0].click();", l)
                time.sleep(1)
                favourite_counts = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div'))).text
            except Exception as e:
                print('Error getting Favourite counts: ',e)                
            try:
                
                driver.get(f"https://twitter.com/{user}/lists")
                list_count = 0
                for i in range (1,10):
                    try:
                        s = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[{i}]/div/div/div/div/div[1]/div[2]')))
                        list_count = list_count + 1
                    except Exception as e:
                        break                
            except Exception as e:
                print("Error Occured in Lists",e)    
            tweet_frequency =[]
            #if tweetno < 1000:
            #    tweetno1=tweetno*.4
            #elif tweetno<5000:
            #    tweetno1=tweetno*.3
            #elif tweetno<10000:
            #    tweetno1=tweetno*.2
            #elif tweetno>10000:
            #    tweetno1=tweetno*0.05
            try: 
                 # Creating list to append tweet data to
                 tweets_list1 = []
                 tweets_list2=[]
                 # Using TwitterSearchScraper to scrape data and append tweets to list
                 for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()):
                     if i>250:
                         break
                     tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
                 #    tweets_list2.append(tweet.date)
                     
                     #tweet_frequency.append(tweet.date)
                 #print(tweets_list2)   
                 # Creating a dataframe from the tweets list above 
                 tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
                 tweets_df1.to_csv(f'Tweets/Real_Id.csv', sep=',', index=False)
                 #tweets_df2 = pd.DataFrame(tweets_list2)
                 print("fetched tweets-------------------------")
                                 #os.system(f"snscrape --format '{content!r}' --max-results 100 twitter-search 'from:{user}'> {user}-tweets.json")
            except Exception as e:
                 print("-----cannot fetch tweets---")
            try:
                print("Full Name : ", Full_name)
                print("Following : ", following)
                print("Followers : ", followers)
                print("Location : ", location)
                print("Join date : ", join_date)
                print("Birth date : ", birthday)
                print("Description : ", desc)
                print("Description : ", tweetno)
                print("Website : ", website)
                print("Favourites_Count : ", favourite_counts)
                print("List_Count : ", list_count)
                #print("Website : ", website)
                print("Verification Status: ", verification)
                #users_info[user] = [Full_name,user,following, followers, join_date, birthday, location, website, desc, tweetno, verification]
              #  Profiles_header = ['Full-name','User-name', 'following', 'followers', 'location','join_date','birthday','bio','website','Tweet no ', 'verification']
                Profiles_data = [ Full_name ,user , following , followers , location, join_date, birthday, desc, website, tweetno, favourite_counts,list_count, verification]
               # dict1 =  {'Full_name':Full_name, 'User-name':user, 'Following':following, 'Followers':followers, 'Location':location,'join-date':join_date,'birthday':birthday,'description':desc,'website':website,'tweetno':tweetno,'verification':verification, 'List_count':list_count}
                #tweet_frequency1=tweets_list2
                with open('Profiles/Profiles_Real.json', 'a', encoding='utf-8') as file:
                    json.dump(Profiles_data,file )
                print("----------Data printed to json file")
            except Exception as e:
                print("Exception of writing To Profiles.json File", e)
            #try:
                
            #    df = pd.read_csv(f'Tweets/{user}.csv')
            #    matrix2 = df[df.columns[0]].as_matrix()
            #    tweet_frequency1= matrix2.tolist()
            #    print(type(tweet_frequency1))
            #except Exception as e:
            #    print("Exception in Tweet Freq: ",e)
            #try:
            #    with open(f'Tweets/{user}.csv','w', encoding='utf-8') as file:
            #        file.write(json.dumps(data_dict, indent = 4))

                    #file.write(tweet_frequency1)
                    #json.dump(tweet_frequency1,file )
             #   print("----------Data printed to Tweet_Freq.json file")
            #except Exception as e:
            #    print("Error in Tweet Frequency : ",e)
            try:
                 driver1 = uc.Chrome(use_subprocess = True )
                 driver1.get(f"https://twitter.com/{user}/photo")
                 time.sleep(3)
                 driver1.save_screenshot(f"D:\FYP\Scweet-master\yo\{user}.png")
                 time.sleep(1)
                 driver1.quit()
                 driver1.close()
                 URL = f"https://unavatar.io/twitter/{user}"
            except Exception as e:
                 print("Error in Getting Image,",e)
            #     response = requests.get(URL)
            #     
            #     open(f"images/{user}-profilepic.png", "wb").write(response.content)
            #     URL2 = f"https://twitter.com/{user}/header_photo"
            #     response = requests.get(URL2)
            #     
            #     open(f"images/{user}-coverpic.png", "wb").write(response.content)
            #     print("fetched Images----------------")
            
            # except Exception as e:
            #         print("Cannot fetch images")
            
            if a == len(users) - 1:
                print(i,len(users))
                driver.close()
                driver.quit()
                return users_info
        else:
            print(" ")
            continue
        a=a+1
        sleep(1)
            
def log_user_page(user, driver, headless=True):
    driver= utils.init_driver(headless=False)
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
    driver = utils.init_driver(headless=True)
    driver.get(f"https://twitter.com/search?q={user}&src=typed_query&f=user")
    list_of_users_get = []
    for i in range(1,28):
        q = WebDriverWait(driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/a/div/div/span')))
        print(q.text)
  
