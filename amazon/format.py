import json
AMAZON_PUT_REQUEST = "PutRequest"

# Load the JSON data from the file
with open("exercises.json", "r") as json_file:
    data = json.load(json_file)

# Initialize an empty list to store the DynamoDB items
items = []

# Iterate over the exercises in the JSON data
count = 0
level = 0
table_name = 'ExerciseData'

primary_key = "ExerciseName"
sort_key = "ExerciseGroup"

dynamodb_json = {}
dynamodb_json[table_name] = []
#while(count % 25 != 0):
for group, group_data in data["Exercises"]["Group"].items():
    for category, category_data in group_data.items():
        for exercise in category_data:
            count += 1
            # Create a new DynamoDB item
            item = {
                "PutRequest": {
                    "Item": {
                        primary_key : {
                            "S": exercise
                        },
                        sort_key : {
                            "S": category
                        },
                        "ExerciseCategory": {
                            "S": group
                        }
                    }
                }
            }
                
            # Add the item to the list
            temp_json = {
            "PutRequest": {
                "Item": item
                }
            }
            dynamodb_json[table_name].append(temp_json)
            if(count % 25 == 0):
                with open("formatted_exercises_{}.json".format(level),"w") as json_file:
                    json.dump(dynamodb_json,json_file,indent=4)
                dynamodb_json[table_name] = []
                level +=1

with open("formatted_exercises.json","w") as json_file:
    json.dump(dynamodb_json,json_file,indent=4)

# Convert the list of items to JSON
# dynamodb_json = json.dumps(items)



# temp_json = {}
# for item in items:
#     print(item)
    
    #print(temp_json)
    
    #print(json.dumps(dynamodb_json[table_name],indent=4))
# print(dynamodb_json[table_name])
#print(json.dumps(dynamodb_json[table_name],indent=4))

# # print the json file
# print(dynamodb_json)
