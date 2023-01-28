import sys
import time
import os
import requests
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Util import Util

#TODO: more filters to recipe generation
# add options for users to specify

class Recipe(Util):

    def __init__(self):
        super().__init__()
        self.debug = True
        self.pantry_data = {} 
        self.spoonacular_api = os.getenv("SPOONACULAR_API")
        self.number_of_recipes = 5
        self.ingredients = str()
        self.spoonacular_info = {
            "complexSearch": {
                "endpoint" : "https://api.spoonacular.com/recipes/complexSearch?apiKey={}".format( self.spoonacular_api),
                
                "options":{
                    "required": {
                        "number": int,
                    },
                    "optional": {
                        "query": str,
                        "cuisine": str,
                        "intolerances": str,
                        "type": str,
                        "equipment": str,
                        "includeIngredients": str,
                        "excludeIngredients": str,
                        "ignorePantry": bool,
                        "fillIngredients": bool,
                        "maxCalories": int,
                        "minCalories": int,
                        "minFat": int,
                        "maxFat": int,
                        "minAlcohol": int,
                        "maxCarbs": int,
                        "minCarbs": int
                        
                    }
                }            
            },

            "findByNutrients":{
                "endpoint": "https://api.spoonacular.com/recipes/findByIngredients?apiKey={}".format(self.spoonacular_api),

                "options":{    
                    
                    "required":{

                    },
                    "optional":{
                        "maxCalories": int,
                        "minCalories": int,
                        "minFat": int,
                        "maxFat": int,
                        "minAlcohol": int,
                        "maxCarbs": int,
                        "minCarbs": int,
                        "minCaffeine": int,
                        "maxCaffeine": int,
                        "maxCalcium": int,
                        "minCalcium": int,
                        "minVitaminA": int,
                        "minVitaminB": int,
                        "minVitaminC": int,
                        "minVitaminD": int,
                        "minVitaminE": int,
                        "minVitaminK": int,
                        "minVitaminB1": int,
                        "minVitaminB2": int,
                        "minVitaminB5": int,
                        "minVitaminB3": int,
                        "minVitaminB6": int,
                        "minVitaminB12": int,
                        "minFiber": int,
                        "minFolate": int,
                        "minFolicAcid": int,
                        "minIodine": int,
                        "minIron": int,
                        "minMagnesium": int,
                        "minManganese": int,
                        "minPotassium": int,
                        "minSelenium": int,
                        "minSodium": int,
                        "minSugar": int,
                        "minZinc": int

                    }   
                }
            },
            "informationBulk":{

                "endpoint": "https://api.spoonacular.com/recipes/informationBulk?apiKey={}".format(self.spoonacular_api),
                "options":{

                    "required":{

                    },

                    "optional":{


                    }
                }
            }
        }

    #returns str of recipe
    def gen_recipes(self,data,filter_options):
        #TODO (zane): generate recipes
        self.pantry_data = data
        self.print_debug("generating recipes")
        #list_of_recipes =self.retrieve_recipes_web() 
        #self.number_of_recipes = num_recipes

        #using complexSearch
        return self.spoonacular_gen_recipe(filter_options,"complexSearch")
    
    def get_food_prices(self,data):
        data_str = ""
        total_spending = 0

        for food_item in data["food"]:
            #TODO: add running total date to monthly spending
            #if(food_item["date_bought"] != null):
            if(food_item["price"] != None):
                total_spending += float(food_item["price"])

        return total_spending
    
    def retrieve_recipes_web(self):

        for food_data in self.pantry_data["food"]:
            food_name = food_data["name"]
            driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
            driver.get('https://www.google.com/search?q=lasagna+recipe&hl=en')

            # buffer for everything to load
            time.sleep(10)

            while True:
                # returns True or False. If element is not displayed (False), breaks out of the while loop

                # pardon my french (xpath)
                show_more_button = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/g-section-with-header/div[2]/g-expandable-container/div/div/div/div[5]/div[2]').is_displayed()
                print(show_more_button) # just for debug
                time.sleep(1)
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/g-section-with-header/div[2]/g-expandable-container/div/div/div/div[5]/div[2]'))).click()
                except:
                    pass

                # if show_more_button element becomes False, break the loop
                if show_more_button == False:
                    break

            for index, result in enumerate(driver.find_elements_by_css_selector('.cv2VAd')):
                try:
                    title = result.find_element_by_css_selector('.hfac6d').text 
                except: title = None

                link = result.find_element_by_css_selector('.cv2VAd .v1uiFd a').get_attribute('href') 
                source = result.find_element_by_css_selector('.KuNgxf').text

                try:
                    total_time = result.find_element_by_css_selector('.wHYlTd').text
                except:
                    total_time = None

                try:
                    # stays the list if need to extract certain ingredient
                    ingredients = result.find_element_by_css_selector('.LDr9cf').text.split(',')
                except:
                    ingredients = None

                try:
                    rating = result.find_element_by_css_selector('.YDIN4c').text
                except:
                    rating = None

                try:
                    reviews = result.find_element_by_css_selector('.HypWnf').text.replace('(', '').replace(')', '')
                except:
                    reviews = None

                print(f'{index + 1}\n{title}\n{link}\n{source}\n{total_time}\n{ingredients}\n{rating}\n{reviews}\n')

            driver.quit()
    
    """
    Action: getting ingredients from virtual pantry
    """
    def get_ingredients(self):
        ingredients = []
        formatted_ingredients = str()
        for index,food_item in enumerate(self.pantry_data["food"]):
            data_str = food_item["name"]
            ingredients.append(data_str)
        formatted_ingredients = ",".join(self.ingredients)

        return formatted_ingredients

    """
    Action: generating spoonacular recipe info
    """
    def spoonacular_gen_recipe(self,filter_options,search_type):
        data_str = str()
        id_l = []
        recipe_bulk = "informationBulk"

        
        # getting  
        ingredient_str = self.get_ingredients()
        spoonacular_endpoint = self.get_spoonacular_endpoint(filter_options,search_type,ingredients=ingredient_str)
        
        #getting ids from complex search spoonacular api with filters applied
        r = requests.get(spoonacular_endpoint)
        results = r.json()
        for recipe_found in results["results"]:
            id_l.append(str(recipe_found["id"]))
        formatted_ids = ",".join(id_l)

        #getting recipe information from bulk recipe spoonacular api
        #self.add_spoonacular_params("informationBulk",,)
        # recipe_bulk_endpoint = add_spoonacular_params("informationBulk",)
        recipe_bulk_endpoint = "{}&{}={}".format(self.spoonacular_info[recipe_bulk]["endpoint"],"ids",formatted_ids)
        z = requests.get(recipe_bulk_endpoint)
        recipe_info = z.json()
        return recipe_info

    # def add_spoonacular_params(self,type_search,list_items,param,value):
    #     endpoint = "{}".format(self.spoonacular_info[type_search]["endpoint"])
    #     formatted_endpoint = "{}&{}={}".format(endpoint,param,value)


        
    def get_id_ingredients(self,results):
        id_l =[]
        for recipe in results:
            id_l.append(str(recipe["id"]))
        id_str = ",".join(id_l)
        return id_str


    def get_spoonacular_endpoint(self,filter_options,search_type,ingredients=""):
        #print(filter_options)
        option_endpoint = self.spoonacular_info[search_type]["endpoint"]

        for require_type,dict_options in self.spoonacular_info[search_type]["options"].items():
            for used_commands,value_inputted in filter_options.items():  
                for option, option_type in dict_options.items():

                    # must lower to compare to arg name (since interaction.option only accepts lowercase names)
                    if(option.lower() == used_commands):
                        option_endpoint = "{}&{}={}".format(option_endpoint,option,value_inputted)
                   # elif(used_commands ==)
        print(option_endpoint)
        return option_endpoint


        
    """
    Action: formats and returns for recipe to display items in embed discord
    """
    def get_recipe_info(self,data):
        page_str = ""
        image_url = ""
        title = ""
        instructions = ""
        ingredients = ""
        embed_info = ["title","sourceUrl","image","analyzedInstructions","extendedIngredients","readyInMinutes","healthScore"]

        for key,value in data.items():
            if key in embed_info:

                if(key == "image"):
                    image_url = value

                elif (key == "title"):
                    title = str(value)

                elif(key == "analyzedInstructions"):
                    # assemblying instruction str
                    for instruct_data in data[key]:
                        for num,step_data in enumerate(instruct_data["steps"],1):
                            instructions = instructions + "**Step {}:** ".format(num)+ step_data['step'] + '\n\n' 

                elif(key == "extendedIngredients"):
                    # assemblying ingredients str
                    for item_data in data[key]:
                        ingredients = ingredients + item_data["original"] + "\n"

                # if (key == "summary"):
                #     summary_formatted = ''
                    

                #     # excluding recommendations
                #     # summary_formatted = value.split("If you like this recipe, take a look at these similar recipes")[0]
                #     # print(summary_formatted)
                #     # # replacing formatted html <b>
                #     # summary_formatted = summary_formatted.replace("</b>","")
                #     # print(summary_formatted)
                #     # page_str = page_str + "{}: ".format(key) + str(summary_formatted) + "\n"
                #     # for match in re.findall("(<.*>)",value):
                #     #         summary_formatted = value.replace(match,"")
                #     if(len(summary_formatted) > 1000):
                #         summary_formatted = summary_formatted[0:1000] + "..."
                
                #     print(summary_formatted)
                #     page_str = page_str + "{}: ".format(key) + str(summary_formatted) + "\n"
                else:
                    page_str = page_str + "{}: ".format(key) + str(value) + "\n"

        page_str = "'{}'".format(page_str)
        return (title ,ingredients,instructions,page_str, image_url)
    
