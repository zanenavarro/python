#!/usr/bin/env python3

import sys
from pathlib import Path

path_to_util = "{}/util".format(Path(__file__).parent.parent)
path_to_lib = "{}/lib".format(Path(__file__).parent.parent)

# debug
print(path_to_lib)
print(path_to_util)

sys.path.append(path_to_util)
sys.path.append(path_to_lib)
from amazon import AmazonHelper
from discord_data_class import discord_data_class


class GymHelper(AmazonHelper):

    def __init__(self):
        super(GymHelper).__init__()
        self.debug = True
        self.discord_data_class = discord_data_class()

    # def get_exercises()





    
    
    



