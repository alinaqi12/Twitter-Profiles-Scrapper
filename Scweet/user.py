from pickle import FALSE
import time
import pandas as pd
import os
import datetime

import requests
import json 
import mysql.connector
from Scweet import utils
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import snscrape
import snscrape.modules.twitter as sntwitter
import selenium
from time import sleep
import chromedriver_autoinstaller
import random
import json
import csv 
from CopyingTable import Copy_Table
from csv import DictWriter
import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
#path = 'C:\\Users\\ALI-NAQI\\Downloads\\chromedriver_win32 (1)\chromedriver.exe'
path = "chromedriver.exe"

def string_to_int(s):

    if 'Tweets' in s:
        s = s.replace('Tweets','')
        if ',' in s:
            s = s.replace(',', '')
        if 'K' in s:
            s = s.replace('K', '')
            if '.' in s:
                s=float(s)
                return int(s*1000)
            return int(s)*1000
        if 'M' in s:
            s = s.replace('M','')
            if '.' in s:
                s=float(s)
                return int(s*1000000)
            return int(s) * 1000000
        return int(s)
    if 'Tweet' in s:
        s = s.replace('Tweet','')
        return int(s)
    if 'Likes' in s:
        s = s.replace('Likes','')
        if ',' in s:
            s = s.replace(',', '')
        if 'K' in s:
            s = s.replace('K', '')
            if '.' in s:
                s=float(s)
                return int(s*1000)
            return int(s)*1000
        if 'M' in s:
            s = s.replace('M','')
            if '.' in s:
                s=float(s)
                return int(s*1000000)
            return int(s) * 1000000
        return int(s)
    if ',' in s:
        s = s.replace(',', '')
    if 'K' in s:
        s = s.replace('K', '')
        if '.' in s:
            s=float(s)
            return int(s*1000)
        return int(s) * 1000
    if 'M' in s:
        s = s.replace('M','')
        if '.' in s:
            s=float(s)
            return int(s*1000000)
        return int(s) * 1000000
    
    return int(s)
    
def get_user_information(users,Search_Query,driver=None, Headless=False):
    #print(users)
    conn = mysql.connector.connect(
    host="localhost",
     user="root",
    password="Jaguar@123",
    database="sql_false_flag")
    cursor = conn.cursor()
    a=1
    """ get user information if the "from_account" argument is specified """
    driver = utils.init_driver(headless=Headless)

    ##----              IF YOU WANT TO TEST THIS CODE ON A SINGLE PROFILE THEN UNCOMMENT THE LINE BELOW     ------
    
    #users = ["umarsarfrazch","umarsarfrazch"]
    users_info = {}
    '''
    query=f"SELECT * from UsersProfile where Fullname LIKE '%{Search_Query}%'"
    cursor.execute(query)
    Tempp=cursor.fetchall()
    primary=[]
    for temp in Tempp:
        primary.append(temp[0])      
    uncommon_elements = list(set(primary) ^ set(users))
    print(uncommon_elements )
    common_elements = list(set(primary) & set(users))
    print(common_elements )
    users=uncommon_elements
    '''
    for i, user in enumerate(users):
        flag = 0

        #log_user_page(user, driver)
         
        if user is not None:
            print(a, " :---------------: " + user + " information  :---------------:",i)
            try:
                driver.get(f'https://twitter.com/{user}')
            except Exception as e:
                driver.get(f'https://twitter.com/{user}')    
                time.sleep(1)
            try:
                driver.get(f'https://twitter.com/{user}')
            except Exception as e:
                driver.get(f'https://twitter.com/{user}')
                time.sleep(1)
            try:
                driver.get(f'https://twitter.com/{user}')
            except Exception as e:
                driver.get(f'https://twitter.com/{user}')
                time.sleep(1)            
            time.sleep(1)
            try: 
                #desc= WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@data-testid="UserDescription")]')))
                followww  = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
                #desc=desc.text
            except Exception as e:
                print(f"{user}'s Account is protected or doesnot exist")
                flag =1
                continue
            try:
                follo = WebDriverWait(driver, 16).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(@href,"/following")]/span[1]/span[1]')))
                following = string_to_int(follo.text)
                followers = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH,'//a[contains(@href,"/followers")]/span[1]/span[1]'))).text
                followers =string_to_int(followers)
            except Exception as e:
                print("------------")
                if flag == 0:
                    driver.get(f'https://twitter.com/{user}')
                    print(e)
                #following=""
                #followers=""
                #print(e)

            try:
                element = driver.find_element(By.XPATH,'//div[contains(@data-testid,"UserProfileHeader_Items")]//a[1]')
                website = element.get_attribute("href")
            except Exception as e:
                # print(e)
                website = "n/a"

            try:
                desc = driver.find_element(By.XPATH,'//div[contains(@data-testid,"UserDescription")]').text
            except Exception as e:
                # print(e)
                desc = "n/a"                
            try:
                profession1=driver.find_element(By.XPATH,'//div[contains(@data-testid,"UserProfileHeader_Items")]')
                profession=profession1.find_element(By.XPATH,'//span[contains(@data-testid,"UserProfessionalCategory")]').text
            except Exception as e:
                profession='n/a'
                #print(e)
            try:

                join_date = driver.find_element(By.XPATH,'//div[contains(@data-testid,"UserProfileHeader_Items")]')
                join_date = join_date.find_element(By.XPATH,
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]//span[contains(@data-testid,"UserJoinDate")]').text
            except Exception as e:
                join_date = 'n/a'
            try:
                birthday = driver.find_element(By.XPATH,
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]//span[contains(@data-testid,"UserBirthdate")]').text
                if 'Born' in birthday:
                    birthday=birthday.replace('Born','')
            except Exception as e:
                birthday ='n/a'
            try:
                location = driver.find_element(By.XPATH,
                    '//div[contains(@data-testid,"UserProfileHeader_Items")]//span[contains(@data-testid,"UserLocation")]').text                   
            except Exception as e:
                location='n/a'
            try:
                s = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[2]')))
                s1 = s.is_displayed()
                if s1 is False:
                    verification = 0
                else:
                  verification = 1  
            except Exception as e:
                print('Error ',e)
            try:    
                tweetno = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div").text
                tweetno = string_to_int(tweetno)
            except Exception as e:
                print("Tweets Not found",e)
            try:
                Full_name = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span').text 
            except Exception as e:
                print ('cannot get name')
            try:
                l = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/nav/div/div[2]/div/div[4]/a')
                #print(l.text)
                driver.execute_script("arguments[0].click();", l)
                time.sleep(1)
                favourite_counts = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/div'))).text
                favourite_counts = string_to_int(favourite_counts)
            except Exception as e:
                print('Error getting Favourite counts: ',e)                
            try:
                
                driver.get(f"https://twitter.com/{user}/lists")
                list_count = 0
                for i in range (1,5):
                    try:
                        s = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[{i}]/div/div/div/div/div[1]/div[2]')))
                        list_count = list_count + 1
                    except Exception as e:
                        break                
            except Exception as e:
                print("Error Occured in Lists",e)    
            
            try:
                print("Full Name : ",Full_name)
                print("Following : ", following)
                print("Followers : ",followers)
                print("Location : ", location)
                print("Join date : ", join_date)
                print("Birth date : ", birthday)
                print("Description : ", desc)
                print("Tweet_no : ", tweetno)
                print("Website : ", website)
                print("Favourites_Count : ", favourite_counts)
                print("List_Count : ", list_count)
                print("Profession : ", profession)
                print("Verification Status: ", verification)
                data1=  {'Full_name':Full_name, 'User-name':user, 'Following':following, 'Followers':followers, 'Location':location,'join-date':join_date,'birthday':birthday,'description':desc,'website':website,'tweetno':tweetno,'verification':verification, 'List_count':list_count,'Likes':favourite_counts,'Profession':profession}
                query = "INSERT INTO UsersProfile_Temp (Username, Fullname, Location, Description,Followers,Following,Join_Date,Verification_status,Lists,Likes,Birthday,Profession,Tweets,Website) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                join_date=join_date.replace("joined", "")
                values = (user,Full_name,location,desc,followers,following,join_date,verification,list_count,favourite_counts,birthday,profession,tweetno,website)
                cursor.execute(query, values)
                conn.commit()               
            except Exception as e:
                print("Exception of writing To DATABASE", e)
        else:
            print(" ")
            continue
            
    #Copy_Table( table name ,Temp temp table name)
    
    print("----------Data Sent to DATABASE")
    driver.close()
    driver.quit()
    cursor.close()
    conn.close()
    return users_info    
    
            
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

#get_user_information(['elonmusk','imrankhanpti'],'helo')
