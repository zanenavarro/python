import sys
from pathlib import Path 
import os
import json
from boto3.dynamodb.conditions import Attr



path_to_discord = str(Path(__file__).parent.parent) + "\\discord\\1_0\\lib\\"
path_to_main = str(Path(__file__).parent.parent) + "\\discord\\1_0\\bin\\"
path_to_file = str(Path(__file__).parent.parent) + "\\amazon\\lib"
print(path_to_discord)

sys.path.append(path_to_file)
sys.path.append(path_to_main)
sys.path.append(path_to_discord)

# import recipe
from recipe import RecipeHelper
# from gym import GymHelper
# from discord_data_class import discord_data_class
# from entertainment import EntertainmentHelper
# from receipt_ocr import ReceiptHelper

