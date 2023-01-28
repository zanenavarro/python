from cgitb import text
from dis import dis
from distutils import command
from sqlite3 import Row
from tkinter import *
from tkinter.ttk import Separator
from turtle import width
import webbrowser
from datetime import datetime
from youtubesearch import VideosSearch


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

def youtube_search(search_word):
    write("searching youtube...")
    # search_word = search_word+"full" # searching for full movie or tv show for better results
    # html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_word)
    # video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # print("https://www.youtube.com/watch?v=" + video_ids[0])

    

    videosSearch = VideosSearch(search_word, limit = 2)

    print(videosSearch.result())
        
    # from pprint import PrettyPrinter
    # #from googleapiclient import discovery
    # from apiclient.discovery import build
    # from apiclient import APIClient
    # #from discovery import build
    # api_key = "AIzaSyDqbynQ6jnv1Y6D2u8rB9hiQxIBs8hfKrI"
    # youtube_api = build('youtube','v3',developerKey = api_key)
    # print(type(youtube_api))
    # request = youtube.search().list(q='Countless Storeys',part='snippet',type='video')
    # print(type(request))
    # res = request.execute()
    # from pprint import PrettyPrinter
    # pp = PrettyPrinter()
    # pp.pprint(res)
    # #Print the total number of results
    # request = youtube.search().list(q='Countless Storeys',part='snippet',type='video',maxResults=50)
    # res = request.execute()
    # print('Total items : ',len(res['items']))

def search_all(search_word):
    ##youtube function call
    youtube_search(search_word)
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
    search_entry = entry.get()
    print(search_entry)
    search_all(search_entry)
    '''
    if(search_entry == "netflix"):
        Label(canvas_image_results, image=disneyplus,borderwidth=0).grid(row=search_position_row,column=search_position_col)
        #Label(canvas_results, image=netflix).grid(anchor ="nw" )
    '''


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