#!/usr/bin/env python3

import sys
import time
import os
import sys
import requests
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from discord_data_class import discord_data_class
from boto3.dynamodb.conditions import Attr

# from ..util.AmazonHelper import AmazonHelper
sys.path.append("../util")
from AmazonHelper import AmazonHelper

#TODO: more filters to recipe generation
# add options for users to specify

class RecipeHelper(AmazonHelper):

    def __init__(self):
        super().__init__()
        self.debug = True
        self.spoonacular_api = os.getenv("SPOONACULAR_API")
        self.ingredients = str()
        self.discord_data_class = discord_data_class()
        self.table_name = "FoodPantryData"
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
    def gen_recipes(self, data, filter_options):
        #TODO (zane): generate recipes
        self.pantry_data = data
        self.print_debug("generating recipes")
        #list_of_recipes =self.retrieve_recipes_web() 
        #self.number_of_recipes = num_recipes

        #using complexSearch
        return self.spoonacular_gen_recipe(filter_options,"complexSearch")

    def get_ingredients(self):
        #TODO: dynamo table pull
        # may be absolute since algorithms might use mix of different filters.
        """getting ingredients from amazonDynamoDB
        :return: ingredients_str: String of formatted ingredients from amazonDynamoDb
        :rtype: ingredients_str: <str>

        """
        filter_expression = Attr('ExerciseCategory').contains("chest")
        self.get_data()
        # filter_expression = ""
        # food_l = self.get_data(self.table_name, filter_expression)

        # ingredients_str = ",".join(food_l)
        # return ingredients_str
        # loop through food list
        # return 
    
    def spoonacular_gen_recipe(self):
        """Generating spoonacular recipe info
        :return: discord_data_class
        :rtype: discord_data_class
        """

        id_l = []
        ##### pulling ingredients from get_ingredients
        ingredient_l = self.get_ingredients()
        ingredient_str = ",".join(ingredient_l)


        ##### assemble endpoint and request recipe froom copmplex search to filter ingredients
        recipe_endpoint = "{0}{1}&ingredients={2}".format(
                self.spoonacular_info["complexSearch"]["endpoint"],
                self.spoonacular_api,
                ingredient_str
            )
        
        results_recipe_search = requests.get(recipe_endpoint).json()

        #### grab all recipe spoonacular ids to get detailed instructions of each recipe
        for recipe_found in results_recipe_search["results"]:
            id_l.append(str(recipe_found["id"]))
    

        #### loop list of recipe ids and assemble mass recipe search endpoint
        formatted_ids = ",".join(id_l)
        recipe_bulk_endpoint = "{}&{}={}".format(self.spoonacular_info["informationBulk"]["endpoint"],"ids",formatted_ids)


        #### request info 
        recipe_info = requests.get(recipe_bulk_endpoint)

        print(json.dumps(recipe_info, indent=4))


        #### format into str and append to list (by embed info)
        embed_info = ["title","sourceUrl","image","analyzedInstructions","extendedIngredients","readyInMinutes","healthScore"]
        embed_info
        #FIXME: save off recipe_info here (cache file)
        for recipe_details in recipe_info:
            content_str = ""
            self.discord_data_class.set_title(recipe_details["title"])
            self.discord_data_class.set_image(recipe_details["image"], 50, 50)

            content_str = content_str + "Health Score: {0}\nTime:{1}\n".format(
                    recipe_details["healthScore"],
                    recipe_details["readyInMinutes"]
                )

            self.discord_data_class.load_content(content_str)



        for key, value in data.items():
            if key in embed_info:

                if (key == "image"):
                    image_url = value

                elif (key == "title"):
                    title = str(value)

                elif (key == "analyzedInstructions"):
                    # assemblying instruction str
                    for instruct_data in data[key]:
                        for num,step_data in enumerate(instruct_data["steps"],1):
                            instructions = instructions + "**Step {}:** ".format(num)+ step_data['step'] + '\n\n' 

                elif (key == "extendedIngredients"):
                    # assemblying ingredients str
                    for item_data in data[key]:
                        ingredients = ingredients + item_data["original"] + "\n"


        
      


        # #### return discord_data_class
        # id_l = []
        # recipe_bulk = "informationBulk"

        # # getting  
        


        # #getting ids from complex search spoonacular api with filters applied
        # r = requests.get(spoonacular_endpoint)
        # results = r.json()
        # for recipe_found in results["results"]:
        #     id_l.append(str(recipe_found["id"]))
        # formatted_ids = ",".join(id_l)


        # #getting recipe information from bulk recipe spoonacular api
        # #self.add_spoonacular_params("informationBulk",,)
        # # recipe_bulk_endpoint = add_spoonacular_params("informationBulk",)
        # recipe_bulk_endpoint = "{}&{}={}".format(self.spoonacular_info[informationBulk]["endpoint"],"ids",formatted_ids)
        # z = requests.get(recipe_bulk_endpoint)
        # recipe_info = z.json()

          
        #### use laod_content discord_data_class
        #self.discord_data_class.load_content()
        
        #### return discord_data_class
        return self.discord_data_class

    # def add_spoonacular_params(self,type_search,list_items,param,value):
    #     endpoint = "{}".format(self.spoonacular_info[type_search]["endpoint"])
    #     formatted_endpoint = "{}&{}={}".format(endpoint,param,value)

    """
    Action: formats and returns for recipe to display items in embed discord
    """
    def get_recipe_info(self, data):
        page_str = ""
        image_url = ""
        title = ""
        instructions = ""
        ingredients = ""
        embed_info = ["title","sourceUrl","image","analyzedInstructions","extendedIngredients","readyInMinutes","healthScore"]

        for key, value in data.items():
            if key in embed_info:

                if (key == "image"):
                    image_url = value

                elif (key == "title"):
                    title = str(value)

                elif (key == "analyzedInstructions"):
                    # assemblying instruction str
                    for instruct_data in data[key]:
                        for num,step_data in enumerate(instruct_data["steps"],1):
                            instructions = instructions + "**Step {}:** ".format(num)+ step_data['step'] + '\n\n' 

                elif (key == "extendedIngredients"):
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
    
