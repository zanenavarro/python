import json
import sys
sys.path.append("../lib")
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from entertainment import EntertainmentHelper
from gym import GymHelper
from recipe import RecipeHelper

PUBLIC_KEY = 'YOUR_APP_PUBLIC_KEY_HERE'

recipe = RecipeHelper()
gym = GymHelper()
entertainment = EntertainmentHelper()


def lambda_handler(event, context):
  try:
    body = json.loads(event['body'])
        
    signature = event['headers']['x-signature-ed25519']
    timestamp = event['headers']['x-signature-timestamp']

    # validate the interaction

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    message = timestamp + json.dumps(body, separators=(',', ':'))
    
    try:
      verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
    except BadSignatureError:
      return {
        'statusCode': 401,
        'body': json.dumps('invalid request signature')
      }  
    
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
      return command_handler(body)
    else:
      return {
        'statusCode': 400,
        'body': json.dumps('unhandled request type')
      }
  except:
    raise

def command_handler(body):
  command = body['data']['name']

  if command == 'generate_recipe':
    return recipe.gen_recipes(0)
  else:
    return {
      'statusCode': 400,
      'body': json.dumps('unhandled command')
    }