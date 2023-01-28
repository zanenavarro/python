from multiprocessing.spawn import get_preparation_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from credentials import username
from credentials import password
from credentials import hulu_password
from credentials import hulu_email
from selenium.webdriver.support.ui import Select

import requests
search_word = "demon slayer"
options = Options()
options.headless = False
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--window-size=1920,1200")

import chromedriver_autoinstaller
link = "https://www.hulu.com/hub/home"
#"https://www.netflix.com/browse"

#driver = webdriver.Chrome(executable_path="C:\\Users\\zanen\\Downloads\\chromedriver_win32 on_one\\chromedriver.exe")
driver = webdriver.Chrome(options=options)
driver.get(link)
#driver.find_element(By.ID, value="id_userLoginId").click()
driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/header/nav/div[2]/a").click()
# time.sleep(100)
time.sleep(1.5)
driver.find_element(By.ID, value="email_id").send_keys(hulu_email)
time.sleep(1.5)
driver.find_element(By.ID, value="password_id").send_keys(hulu_password)
time.sleep(1)
driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/button").click()
time.sleep(2)
time.sleep(20)
driver.get("https://www.hulu.com/search")
time.sleep(2)
driver.find_element(By.XPATH, value="/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/input").send_keys(search_word)

time.sleep(1.5)



select = driver.find_element(By.XPATH,value= "//*[@id='instantSearch']")  #get the select element     
options = select.find_elements(By.TAG_NAME,value="li") #get all the options into a list

results = [] 
[results.append(x.text) for x in options if x.text not in results] #all text goes in results

#getting rid of duplicates
final_list = []
for i in results:
    h = i.split("\n")
    final_list.append(h[0])
print(final_list)



#content = driver.find_elements(By.XPATH,value="/html/body/div[2]/div[1]/div[2]/div/div[2]/ul")
# InstantSearch__Option

# for c in content:
#     print(c.get_property("href"))

# first_one = Select(driver.find_elements(By.XPATH,value="/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[1]/a")).select_by_value("href")
# second_one = Select(driver.find_elements(By.XPATH,value="/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[2]/a")).select_by_value("href")
# third_one = Select(driver.find_elements(By.XPATH,value="/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[3]/a")).select_by_value("href")
# optionsList.append(first_one)
# # optionsList.append(driver.find_elements(By.XPATH,value="/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[2]/a").get_property("href"))
# # optionsList.append(driver.find_elements(By.XPATH,value="/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[3]/a").get_property("href"))

# print(optionsList)

# for option in options: #iterate over the options, place attribute value in list
#     optionsList.append(option.get_property("href"))

# for optionValue in optionsList:
#     print("starting loop on option %s",optionValue)

    # select = Select(driver.find_element_by_xpath( "//select[@id='idname']"))
    # select.select_by_value(optionValue)

#driver.find_element(By.XPATH, value="/html/body/div[2]/header/nav/div[2]/a").click()
# /html/body/div[2]/header/nav/div[2]/a
time.sleep(100)


#####################################################################


#signin_name = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div/div/label/label")
# signin_name = driver.find_element(By.ID, value="id_userLoginId").send_keys(username)
# # driver.find_element_by_id("id_userLoginId").send_keys(username)
# # driver.find_element_by_id("id_password").send_keys(password)
# time.sleep(1)
# signin_password = driver.find_element(By.ID, value="id_password").send_keys(password)
# time.sleep(2)
# driver.find_element(By.XPATH,value="/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").click()   #clicking  sign in button   
# time.sleep(4)
# driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[4]/div/a/div/div").click() #clicking boys button 
# time.sleep(2)
# driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button").click()
# time.sleep(1)
# signin_password = driver.find_element(By.ID, value="searchInput").send_keys(search_word)
# time.sleep(2)
# click_movie = driver.find_element(By.ID,value='title-card-0-0').click()
# time.sleep(2)
# first_title = driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/img[2]')
# title_name = first_title.get_property("title")
# image_link = first_title.get_property("src")
# time.sleep(1)
# watchable_link = driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[2]/a").get_property("href")
# print(watchable_link)
# print(title_name)
# print(image_link)
# time.sleep(200)




# print(driver.page_source)
# driver.quit()