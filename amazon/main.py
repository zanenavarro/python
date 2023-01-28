import os




output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_1.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_2.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_3.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_4.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_5.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_6.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_7.json").read()
print(output)
output = os.popen("aws dynamodb batch-write-item --request-items file://formatted_exercises_8.json").read()
print(output)
