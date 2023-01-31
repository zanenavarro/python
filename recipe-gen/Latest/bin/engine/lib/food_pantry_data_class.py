import sys
import json
sys.path.append(r"C:\Users\zanen\OneDrive\Desktop\Projects\Python\recipe-gen\1_0\util")
from Util import Util

class food_pantry_data_class(Util):
    
    def __init__(self,path_to_json=None):

        if(path_to_json == None):
            self.PANTRY_DATA = {
                "food": []
            }
        else:
            self.PANTRY_DATA  = self.get_dictionary(path_to_json)
            print("getting dictionary from file: {}".format(path_to_json))
    


    def get_pantry_data(self):
        return self.PANTRY_DATA
    
    def add_food_item(self,food_data):
        self.PANTRY_DATA["food"].append(food_data)

    def print_pantry_data(self):
        print(json.dumps(self.PANTRY_DATA,indent=4))

    # def get_recipes(self):
    #     self.print_debug("getting items")