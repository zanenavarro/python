# import discord
# from helper import *

# class MyClient(discord.Client):
    
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))
        
#         if((message.content == functions["pull"]) or (message.content == functions["push"]) or (message.content == functions["legs"])):
#             day = message.content.strip('!')
#             listExercises = getExercises(day)
            
#             for i in range(len(listExercises)):
#                 listExercises[i] = str(i) + ": "+ listExercises[i]
                
#             exercises = "\n".join(listExercises)
#             await message.channel.send("`"+exercises+"`")
#         if(functions["add"] in message.content ):
#             listAdd = message.content.lower().split(" ")
#             if(len(listAdd) != 5 and (len(listAdd) < 2)):
#                 #addTodata(day,name, group, position):
#                 await message.channel.send("`"+"incorrect format. use: !add push push-ups chest lower"+"`")
            
#                 if((listAdd[1] == "push") or (listAdd[1] == "pull") or (listAdd[1] == "legs" ) or (listAdd[4] == "lower") or (listAdd[4] == "upper")):    
#                     addTodata(listAdd[1],listAdd[2],listAdd[3],listAdd[4])
#                     await message.channel.send("`"+"added exercise!"+"`")
#         # help function
#         # if((message.content == functions["help"])):
#         #     for key,values in functions.items():
#         #         message_send = "Function List:\n"
#         #         message_send = message_send +"\t"+key+" : "+values+"\n"
#         #     await message.channel.send("`"+message_send+"`")

            