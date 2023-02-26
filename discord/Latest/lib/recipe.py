#!/usr/bin/env python3

import sys
import time
import os
import sys
import requests
import boto3
import json
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from boto3.dynamodb.conditions import Attr

from pathlib import Path

# FIXME : add single file to hold these util and lib - Plugin package

path_to_util = "{}/util".format(Path(__file__).parent.parent)
sys.path.append(path_to_util)

from dotenv import load_dotenv
from amazon import AmazonHelper
from discord_data_class import discord_data_class

BASEDIR = os.path.abspath(os.path.dirname(__file__)) + "\.env"
load_dotenv(BASEDIR)
#TODO: more filters to recipe generation
# add options for users to specify

class RecipeHelper(AmazonHelper):

    def __init__(self):
        super().__init__()
        self.debug = True
        self.spoonacular_api = os.getenv("SPOONACULAR_API")
        self.ingredients = str()
        self.discord_data_class = discord_data_class()
        self.table_name = "FoodPantry"
        self.color = "red"
        #FIXME: possible lib to hold spoonacular info -> import
        self.spoonacular_info = {
            "complexSearch": {
                "endpoint": "https://api.spoonacular.com/recipes/complexSearch?apiKey={}".format(self.spoonacular_api)
            },

            "findByNutrients": {
                "endpoint": "https://api.spoonacular.com/recipes/findByIngredients?apiKey={}".format(self.spoonacular_api)
            },

            "informationBulk": {
                "endpoint": "https://api.spoonacular.com/recipes/informationBulk?apiKey={}".format(self.spoonacular_api),
            }
        }

    def gen_recipes(self):
        """generates recipe
        :return: discord api class 
        :rtype: <discord_data_class>
        """
        return self.spoonacular_gen_recipe()

    def get_ingredients(self):
        """getting ingredients from amazonDynamoDB
        :return: ingredients_str: String of food_items
        :rtype: ingredients_str: <str>
        """
        ingredient_l = []
        # Using db_condition: access to boto3 conditiona
        #TODO: specific methods utilizing more of boto3 condition class
        db_condition = (boto3.dynamodb.conditions.Attr('FoodGroup').ne(0))
        # print(db_condition)
        food_data = self.get_data(self.table_name, db_condition)
        
        for items in food_data:
            # food_group = items["FoodGroup"]
            food_name = items["FoodName"]
            ingredient_l.append(food_name)
            
        return ingredient_l

    def spoonacular_gen_recipe(self):
        """Generating spoonacular recipe info
        :return: discord_data_class
        :rtype: discord_data_class
        """
        id_l = []
        ingredient_l = self.get_ingredients()
        ingredient_str = ",".join(ingredient_l)

        # assemble endpoint for 'complexSearch'
        recipe_endpoint = "{0}&ingredients={1}".format(
                self.spoonacular_info["complexSearch"]["endpoint"],
                ingredient_str
            )

        # Debug
        # print(recipe_endpoint)
        
        results_recipe_search = requests.get(recipe_endpoint).json()

        # debugs
       # print(results_recipe_search)

        # Get list of id for recipes from 'complexSearch'
        for recipe_found in results_recipe_search["results"]:
            id_l.append(str(recipe_found["id"]))

        # assemble endpoint for 'informationBulk'
        formatted_ids = ",".join(id_l)
        recipe_bulk_endpoint = "{0}&ids={1}".format(
                self.spoonacular_info["informationBulk"]["endpoint"],
                formatted_ids
            )

        recipe_info = requests.get(recipe_bulk_endpoint).json()
        description_str = ""

        # loading discord api class
        for recipe_data in recipe_info:
            # TODO: create desciption with more info
            # TODO: can this be solved in a more intuitive way
            description_str += recipe_data["summary"]

            self.discord_data_class.set_embed_color(self.color)
            self.discord_data_class.set_embed_title(recipe_data["title"])
            self.discord_data_class.set_embed_image(recipe_data["image"], 20, 20)
            self.discord_data_class.set_embed_description(description_str)
            self.discord_data_class.load_embed_content()
        
        return self.discord_data_class

    