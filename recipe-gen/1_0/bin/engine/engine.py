import sys
import json
from pathlib import Path

path_to_file = str(Path(__file__).parent)
path_to_data_class = "{}/lib".format(path_to_file)
path_to_bin = "{}/bin".format(path_to_file)

# food pantry data class
sys.path.append(path_to_data_class)

# recipe and receipt_ocr
sys.path.append(path_to_bin)


from Util import Util
from recipe import Recipe
from food_pantry_data_class import food_pantry_data_class
from receipt_ocr import Receipt_ocr

class Engine(Util):
    def __init__(self):
        super().__init__()
        self.receipt_ocr = Receipt_ocr()
        self.recipe = Recipe()
        self.pantry_dc = food_pantry_data_class(self.pantry_path)

    def run(self,message):
        self.print_debug("fetching message")

    def get_recipe(self):
        data_str = self.recipe.gen_recipe(self.pantry_dc.get_pantry_data())
        return data_str

    def register_receipt(self,image_url):
        data = self.receipt_ocr.process_image(image_url)
        for item in data["food"]:
            self.pantry_dc.add_food_item(item)
        self.print_dictionary(self.pantry_path,self.pantry_dc.get_pantry_data(),"w")


    def get_food_items(self):
        data = self.pantry_dc.get_pantry_data()
        data_str = ""
        #print(json.dumps(data,indent=4))
        for food_data in data["food"]:
            data_str = data_str +" - "+ food_data["name"] + "\n"
        return data_str
    
    def gen_recipe(self,filter_commands):
        return self.recipe.gen_recipes(self.pantry_dc.get_pantry_data(),filter_commands)

    def get_budget_items(self):
        return self.recipe.get_food_prices(self.pantry_dc.get_pantry_data())
        


