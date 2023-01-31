import json
import datetime

class Util():
    def __init__(self):
        self.debug = True
        self.pantry_path = r"C:\Users\zanen\OneDrive\Desktop\Projects\Python\recipe-gen\1_0\lib\virtual_pantry.json"

    
    def get_dictionary(self,path_to_json):
        data = {}
        with open(path_to_json,"r") as json_file:
            data = json.load(json_file)
        return data

    def print_debug(self,message):
        date = datetime.datetime()
        today = date.now()
        date_str = today.strftime("%c")
        file = open("discord.log")
        if(self.debug):
            file.write("{}: discord_bot {}")
            print(message)
        

    def print_dictionary(self,path,data,character):
        with open(path,character) as json_file:
            json.dump(data,json_file,indent=4)
            json_file.close()
        

    def create_log_file(self):
        log_str =""
        with open("discord.log","w") as log_file:
            log_file.write(log_str)
            log_file.close()
    
    def get_log_file_data(self):
        data_str = ""
        with open("discord.log","r") as log_file:
            data_str = log_file.read()
            log_file.close()
        return data_str

