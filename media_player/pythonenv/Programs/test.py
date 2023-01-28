from ast import arg
from cgitb import text
from dis import dis
from distutils import command
from importlib.resources import path
from sqlite3 import Row
from tkinter import *
from tkinter.ttk import Separator
from turtle import width
#from typing_extensions import Self
from unittest import result
import webbrowser
from datetime import datetime
from requests import request
from youtube_search import YoutubeSearch
import json
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from credentials import username, password,hulu_email,hulu_password
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
import threading
import logging
import time


netflix_result = str()
youtube_result = str()
hulu_result = str()
search_word = str()
# hbomax_result
# disney_result

#import thread

#now = datetime.now() # current date and time
  
#### Main Window ########################
#########################################
master = Tk()
master.geometry("1485x875+10+20")
master.configure(bg='#00A2E8')
master.title("Zane's Media Center")
search_position_row = 0
search_position_col = 0



#### Canvases #############################
###########################################
#canvas = Canvas(master,background='#22B14C')

## Canvas Top of Window (split into three rows) ##
canvas = Canvas(master,background='orange')
canvas.grid(row=0, column=0,sticky='N')


## Canvas Bottom of Window (split into three rows) ##
canvas_results = Canvas(master,background='#00A2E8',width=30,height=30)
canvas_results.grid(row=2,column =0)
canvas_results.pack_propagate(False)


## Canvas Middle of window (split into three rows) ##
canvas_middle = Canvas(master,background='#00A2E8',width=1400,height=100)
canvas_middle.grid(row=1, column=0,padx=5, pady=10,sticky='e') # sticky='E'
canvas_middle.pack_propagate(False)

## Canvas holding settings, account and sort and search entry ##
canvas_entry = Canvas(canvas_middle,background='white',width=1200,height=60)
canvas_entry.grid(row=1, column=1,padx=5, pady=10) # sticky='E'
canvas_entry.pack_propagate(False)

## Canvas Art for Logo ##
canvas_art = Canvas(canvas_middle,height= 80, width=600,background='white')
canvas_art.grid(row=1,column =0,padx=90, pady=10,sticky="")
canvas_art.pack_propagate(False)

## Canvas Console ##
canvas_console = Canvas(canvas_results,background='white')
canvas_console.grid(row=1,column=0,padx=5, pady=10)
canvas_console.pack_propagate(False)
## Canvas results ##
canvas_image_results = Canvas(canvas_results,background='orange',height=415,width=1425)
canvas_image_results.grid(row=0,column=0)
canvas_image_results.pack_propagate(False)


#### Console ############################################
#########################################################
scrollbar= Scrollbar(canvas_console,highlightcolor='black')
mylist = Listbox(canvas_console,width=178,height=4,background='black',activestyle='none',selectbackground='black')
mylist.configure(background="black", foreground="white", font=('Consolas 11'),highlightcolor='black')
mylist.grid(row=7,column=1,rowspan=3, sticky='e')
scrollbar.grid(row=7, column=2, rowspan=3, sticky='nsw')


#### Images #############################################
#########################################################
disneyplus= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\disneyplus_og_200.png")
netflix = PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\netflix_200.png")
hulu= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\hulu-squarelogo.png")
hbomax= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\hbomax_og_200.png")
peacock= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\peacock_og_200.png")
primevideo= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\prime_video_og_200.png")
youtube= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\youtube_og_200.png")
image_list = [disneyplus,netflix,hulu,hbomax,peacock,primevideo,youtube]


#### Handling Functions ###############################
#######################################################

import urllib.request
import re



def write(message):
    now = datetime.now()
    mylist.insert("end", now.strftime("%H:%M:%S") + ": "+ message)
    #mylist.select_clear(mylist.size() - 2)   #Clear the current selected item     
    mylist.select_set(END)                             #Select the new item
    mylist.yview(END)                                  #Set the scrollbar to the end of the listbox


def youtube_search():
    write("hello christina")
    write("searching youtube...")
    # global youtube_result
    search_word = get_search_word()
    # link = "https://www.youtube.com/results?search_query="+search_word
    # results = requests.get(link)
    # print(results.json())

    from youtubesearchpython import Search
    allSearch = Search(search_word, limit = 1)
    title = allSearch.result()["result"][0]["title"]
    id = allSearch.result()["result"][0]["id"]
    watchable_link= "https://www.youtube.com/watch?v="+id

    print("Youtube Result) Title: %s : link: %s" % (title,watchable_link)) 
    # returns dict of search results for youtuibe
    # can do something later on like attach new button directlky to fgirst searchg result

    # from youtubesearchpython import VideosSearch

    # videosSearch = VideosSearch(search_word, limit = 10)
    # print(videosSearch.result())





    # results = YoutubeSearch(search_word, max_results=10).to_json()
    # main_dict = json.loads(results)
    # print(main_dict)
    # list_ids = []
    # list_thumbnails = []
    # list_titles = []
    # list_duration = []
    # for num in range(len(main_dict["videos"])):
    # #     print(main_dict[i])

    #     list_ids.append(main_dict["videos"][num]["id"])
    #     list_thumbnails.append(main_dict["videos"][num]["thumbnails"][0])
    #     list_titles.append(main_dict["videos"][num]["title"])
    #     list_duration.append(main_dict["videos"][num]["duration"])

    # for i,item in enumerate(results):
    #     print(results[i]["id"])  
    
    # print(list_thumbnails)
    #print(list_titles[0])
    

def netflix_search():
    search_word = get_search_word()
    write("searching netflix...")

    options = Options()
    #options = ChromeOptions()
    options.headless = True
    #options.add_experimental_option("excludeSwitches", ["enable-logging"])    
    #profile_link ="C:\\Users\\zanen\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"  # profile 1 since user-data-dir is used already need to creast environment where selenium can operate independtly
    profile_link = "C:\\Users\\zanen\\AppData\\Local\\Google\\Chrome\\altProfile\\Profile 1"    
    options.add_argument("profile-directory=SETH")
    options.add_argument("user-data-dir="+profile_link)
    options.add_argument("--window-size=1920,1200")
    #currently at seth profile google
    #path ="C:\Program Files\Google\Chrome\Application"
    path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    #path = "C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Programs\\chromedriver.exe"
    
    driver = webdriver.Chrome(service=Service(executable_path=path),options=options)
    time.sleep(1)
    driver.get("https://www.netflix.com/browse")
    # C:\Users\zanen\AppData\Local\Google\Chrome\User Data\Default
    # "C:\Users\zanen\AppData\Local\Google\Chrome\User Data\Default"
    # update would be to have user create profile or ask user for sign in info in settings and update and save login info to be used 
    
    # time.sleep(3)
    # signin_name = driver.find_element(By.ID, value="id_userLoginId").send_keys(username)
    # time.sleep(1)
    # signin_password = driver.find_element(By.ID, value="id_password").send_keys(password)
    # time.sleep(2)
    # driver.find_element(By.XPATH,value="/html/body/div[1]/div/div[3]/div/div/div[1]/form/button").click()   #clicking  sign in button   
    # time.sleep(4)
    # driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[4]/div/a/div/div").click() #clicking profile button 
    # time.sleep(2)
    driver.find_element(By.XPATH,value="/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/button").click()  #clicking search tab
    time.sleep(1)
    signin_password = driver.find_element(By.ID, value="searchInput").send_keys(search_word)       # inputting searchword
    time.sleep(2)
    click_movie = driver.find_element(By.ID,value='title-card-0-0').click()                 #getting first search results
    time.sleep(2)
    first_title = driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/img[2]') #title results info
    title_name = first_title.get_property("title")
    image_link = first_title.get_property("src")    #title imagelink (potential downloadand show image on media player) additional thing todo / using time= slowerforuser 
    time.sleep(1)
    watchable_link = driver.find_element(By.XPATH,value="/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[2]/a").get_property("href") #link to netflix (play link)- for future use
    # print(watchable_link)
    # print(title_name)
    print("Netflix Result) Title: %s : link: %s" % (title_name,watchable_link))
    # print(image_link)
    #watchable_link

def hulu_search():
    write("searching hulu...")
    search_word = get_search_word()
    global hulu_result
    options = Options()
    options.headless = False
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--window-size=1920,1200")
    link = "https://www.hulu.com/hub/home"
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/header/nav/div[2]/a").click()
    time.sleep(1.5)
    driver.find_element(By.ID, value="email_id").send_keys(hulu_email)
    time.sleep(1.5)
    driver.find_element(By.ID, value="password_id").send_keys(hulu_password)
    time.sleep(1)
    driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div/button").click()
    time.sleep(2)
    time.sleep(15)
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
    #print(final_list[0])



def peacock_search(search_word):
    write("searching peacock...")

def disney_search(search_word):
    write("searching disney...")

def hbomax_search(search_word):
    write("searching hbomax...")


def search_all():
    #global search_word
    ##youtube function call
    print("word entered: ",search_word)
    threading.Thread(target=youtube_search).start()    # youtube thread
    threading.Thread(target=netflix_search).start()    # netflix thread
    #threading.Thread(target=hulu_search).start()       # hulu thread
    # threading.Thread(target=peacock_search,args=search_word).start()    # peacock thread
    # threading.Thread(target=disney_search,args=search_word).start()    # disney thread
    # threading.Thread(target=hbomax_search,args=search_word).start()    # hbomax thread

    ##netflix function call
    #netflix_search(search_word)
    ##hulu function call
    #hulu_search(search_word)


def netflix_push():
    webbrowser.get().open_new_tab("https://netflix.com")
    write("opening netflix...")

def disney_push():
    webbrowser.get().open_new_tab("https://www.disneyplus.com/")
    write("opening disney...")

def hbomax_push():
    webbrowser.get().open_new_tab("https://www.hbomax.com/")
    write("opening hbomax...")
def hulu_push():
    webbrowser.get().open_new_tab("https://hulu.com")
    write("opening hulu...")

def primevideo_push():
    webbrowser.get().open_new_tab("https://www.amazon.com/Prime-Video/b?node=2676882011")
    write("opening prime video...")

def peacock_push():
    webbrowser.get().open_new_tab("https://peacocktv.com")
    write("opening peacock...")

def youtube_push():
    webbrowser.get().open_new_tab("https://youtube.com")
    write("opening youtube...")

def search_button():
    update_word(entry.get())
    #print(search_entry)
    set_search_word(entry.get())
    search_all()
    '''
    if(search_entry == "netflix"):
        Label(canvas_image_results, image=disneyplus,borderwidth=0).grid(row=search_position_row,column=search_position_col)
        #Label(canvas_results, image=netflix).grid(anchor ="nw" )
    '''
def update_word(word):
    global search_word
    search_word = word
def set_search_word(word):
    global search_word
    search_word = word
def get_search_word():
    global search_word
    return search_word


command_list = [disney_push, netflix_push, hulu_push, hbomax_push, peacock_push, primevideo_push, youtube_push]


#### Buttons for Services ################################
##########################################################

for i in range(7):
    button_show = Button(canvas, image=image_list[i],command=command_list[i],borderwidth=0)
    button_show.grid(row=0,column=i,padx=5, pady=10)


#### Middle Menu and Search ###########################
#######################################################
def setting_clicked():
    print("SETTING BUTTON: potential settings feature: open new window function go here...")
    # creating setting window 
    setting = Toplevel(master)
    setting.geometry("1150x500+10+20")
    setting.title("Settings")


def account_chrome_clicked():
    print("ACCOUNT BUTTON: open chrome browser function. Potential opening all streaming service sign in page?")

def sort_clicked():
    print("SORT BUTTON: window opens to sort the search")

## Settings ##
settings_photo = PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\settings_og_60.png")
settings_icon= Button(canvas_entry,image=settings_photo,command=setting_clicked)
settings_icon.grid(row=0,column = 2,padx= 10, pady=3)
## Account ##
account_photo = PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\user_og_60.png")
account_icon= Button(canvas_entry,image=account_photo,command=account_chrome_clicked)
account_icon.grid(row=0,column = 1,padx= 10, pady=3)
## Sort ##
sort_photo= PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\sort_og_60.png")
sort_icon= Button(canvas_entry,image=sort_photo,command=sort_clicked)
sort_icon.grid(row=0,column = 0,padx= 10, pady=3)
## Entry ##
entry = Entry(canvas_entry,width=60)
entry.grid(row = 0, column = 3, pady = 2)
## Search Button ##
search_button= Button(canvas_entry,text="Search",command=search_button)
search_button.grid(row = 0, column = 4,padx = 5, pady = 4)

## Art ##
cloud_photo = PhotoImage(file=r"C:\\Users\\zanen\\OneDrive\\Desktop\\Projects\\Python\\media_player\\pythonenv\\Images\\seven_piece_og.png")
cloud_icon = Label(canvas_art,image=cloud_photo)
cloud_icon.pack()





###Update list box


#button.grid(row=0,column=1,pady=3)
# button0.pack()
# button1.pack(side=LEFT, anchor=NW)
# button2.pack()
# button3.pack()
# button4.pack()
# button5.pack()
# button6.pack()



mainloop()