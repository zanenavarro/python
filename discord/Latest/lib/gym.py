#!/usr/bin/env python3


import sys
sys.path.append("../util")
from amazon import AmazonHelper
from discord_data_class import discord_data_class


class GymHelper(AmazonHelper):

    def __init__(self):
        super(GymHelper).__init__()
        self.debug = True
        self.discord_data_class = discord_data_class()


    # def get_exercises()





    
    
    



