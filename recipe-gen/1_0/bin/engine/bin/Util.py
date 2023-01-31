import json
from pathlib import Path
from datetime import datetime


path_to_file = str(Path(__file__).parent.parent)
path_to_pantry = "{}/lib/virtual_pantry.json".format(path_to_file)

class Util():
    def __init__(self):
        self.debug = True
        self.pantry_path = path_to_pantry
        self.create_log_file()

    
    def get_dictionary(self,path_to_json):
        data = {}
        with open(path_to_json,"r") as json_file:
            data = json.load(json_file)
        return data

    def print_debug(self,message):
        # datetime object containing current date and time
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y %H:%M:%S")
    
        if(self.debug):
            print(message)
            with open("discord.log","w") as log_file:
                log_file.write("{}: discord_bot {}".format(date_str,message))
        

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
