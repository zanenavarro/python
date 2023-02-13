import sys
import veryfi
import base64
import requests
import json
import re
import shutil
import os
from dotenv import load_dotenv
load_dotenv()
from discord_data_class import discord_data_class
import sys
sys.path.append("../util")
from amazon import AmazonHelper
print(AmazonHelper)


class ReceiptHelper(AmazonHelper):

    def __init__(self):
        super().__init__()
        self.discord_data_class = discord_data_class()

    def process_image(self, image_url):
        self.print_debug("running")
        # verify client ocr api info
        client_id = os.getenv("VERIFY_CLIENT_ID")
        client_secret = os.getenv("VERIFY_CLIENT_SECRET")
        username = os.getenv("VERIFY_USERNAME")
        api_key = os.getenv("VERIFY_API_KEY")
        client = veryfi.Client(client_id,client_secret,username,api_key)

        file_name = image_url.split("/")[-1]
        res = requests.get(image_url, stream = True)
        if res.status_code == 200:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')
        #TODO : switch to control client process may be helpful
        json_result = client.process_document(file_name)


    # adding food items to food pantry
        data = {"food": []}
        for item_data in json_result["line_items"]:
            food_details = {}

            text_line = item_data["text"]
            item_name = re.split(r'\t+', text_line)[0]

            food_details["name"] = item_name
            food_details["price"] =  item_data["price"]
            food_details["quantity"] = item_data["quantity"]
            food_details["date_bought"] = item_data["date"]

            data["food"].append(food_details)
        #self.pantry_dc.print_pantry_data()

        #debug
        self.print_dictionary(r"C:\Users\zanen\OneDrive\Desktop\Projects\Python\recipe-gen\1_0\lib\commands.json",json_result,"a")
        #self.print_dictionary(r"C:\Users\zanen\OneDrive\Desktop\Projects\Python\recipe-gen\1_0\lib\virtual_pantry.json",self.pantry_dc.get_pantry_data(),"w")
        return data
