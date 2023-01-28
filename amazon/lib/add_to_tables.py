# import boto3
# import json

# # Create a boto3 client for DynamoDB
# dynamodb = boto3.client('dynamodb')

# # Load the JSON file
# with open('exercises.json') as file:
#     exercises = json.load(file)

# # Iterate through the items in the JSON file and insert them into the DynamoDB table
# for group in exercises['Exercises']:
#     for category in exercises['Exercises'][group]:
#         for sub_category in exercises['Exercises'][group][category]:
#             print(sub_category)
#             for exercise in exercises['Exercises'][group][category][sub_category]:
               
#                 item = {
#                     'Exercises': {
#                         'group': {'S': group},
#                         'category': {'S': category},
#                         'subcategory': {'S': sub_category},
#                         'name': {'S': exercise},
#                     }
#                 }
#                 dynamodb.put_item(TableName='Exercises', Item=item)
import json
import boto3
import time

AMAZON_STRING = 'S'

dynamodb = boto3.client('dynamodb')

# Load the JSON file
with open('back_exercises.json') as json_file:
    list_exercises = json.load(json_file)




# Iterate through the exercises and build dictionary used for 'response' paramter
count = 0
for exercises in list_exercises:
    amazon_format = {}
  
    
    print(exercises)
    # for subcategory,exercise_info in exercises.items():
    '''
    # building dictionary

    Amazon standard:
        'Group': {'S': exercise['Group']['S']},
        'Category': {'S': exercise['Category']['S']},
        'Name': {'S': exercise['Name']['S']},
    
    '''
        # amazon_format[subcategory] = {}
        # # print(info_category)
        # info_category = exercise_info[AMAZON_STRING]
        #amazon_format[subcategory]['S'] = info_category
    response = dynamodb.put_item(
        TableName='Exercises',
        Item=exercises
    )
    time.sleep(.2)
    count += 1

#debug
print(json.dumps(amazon_format,indent=4))
# for dynamo_item in amazon_format:
    # print()
    # every item in built dicitonary
    

# print(response)
print('Inserted {} exercises into DynamoDB table'.format(count))
