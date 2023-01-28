import json

with open('formatted_exercises.json') as f:
    data = json.load(f)

for category in data['Exercises']:
    for sub_category in data['Exercises'][category]:
        for type_ in data['Exercises'][category][sub_category]:
            for exercise in data['Exercises'][category][sub_category][type_]:
                print(exercise['name'])
