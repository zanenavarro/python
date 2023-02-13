import json
import sys
import os
sys.path.append("../lib")
# from nacl.signing import VerifyKey
# from nacl.exceptions import BadSignatureError
from entertainment import EntertainmentHelper
from gym import GymHelper
from recipe import RecipeHelper
from discord_data_class import discord_data_class

PUBLIC_KEY = os.getenv("DISCORD_A")

recipe = RecipeHelper()
gym = GymHelper()
etertainment = EntertainmentHelper()

# context :todo
def lambda_handler(event):
  try:
    body = json.loads(event['body'])
  
    # signature = event['headers']['x-signature-ed25519']
    # timestamp = event['headers']['x-signature-timestamp']

    # validate the interaction

    # verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    # message = timestamp + json.dumps(body, separators=(',', ':'))
    
    # try:
    #   verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
    # except BadSignatureError:
    #   return {
    #     'statusCode': 401,
    #     'body': json.dumps('invalid request signature')
    #   }  
    
    # handle the interaction

    t = body['type']

    if t == 1:
      return {
        'statusCode': 200,
        'body': json.dumps({
          'type': 1
        })
      }
    elif t == 2:
      return command_handler(t, body)
    else:
      return {
        'statusCode': 400,
        'body': json.dumps('unhandled request type')
      }
  except:
    print("raised exception")
    raise


def command_handler(type, body):
  """handles commands & returns correct body to be returned to discord 

  (TODO): async 'loading' embed... 
  :return: None
  """
  command = body['data']['name']

  if (command == 'generate_recipe'):
    discord_dc = recipe.gen_recipes()
    return discord_dc.get_message(type)

  else:
  
    return {
      'statusCode': 400,
      'body': json.dumps('unhandled command')
    }