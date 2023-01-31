import interactions
import sys
import os
import asyncio
import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = interactions.Client(token=os.getenv("BOT_TOKEN"))
current = 0
previous_count = current


from pathlib import Path

path_to_engine = Path(__file__).parent / "engine" 
sys.path.append(str(path_to_engine))
from engine import Engine

engine = Engine()

#################### HELPER FUNCTION ##########################

def get_type_interaction(type_to_convert):
    type_interaction = interactions.OptionType.STRING
    print(type_to_convert)
    if(type(type_to_convert) == str):
        type_interaction = interactions.OptionType.STRING
    elif(type(type_to_convert) == int):
        type_interaction = interactions.OptionType.INTEGER
    elif(type(type_to_convert) == bool):
        type_interaction = interactions.OptionType.BOOLEAN
    print(type_interaction)
    return type_interaction


##############################################################
####### HELP COMMAND ################################################

@bot.command(

    name="help",
    description="shows list of commands and how to use",
    # options=[
    #             interactions.Option(
    #                 name="img_file",
    #                 description="image of receipt grocery store.",
    #                 type=interactions.OptionType.ATTACHMENT,
    #                 required=True,
    #             ),
    #         ]
)


async def help(ctx: interactions.CommandContext):
    data_str = ""
    title = "FUNCTIONS\n"
    spacer = " "

    data_str = data_str + spacer + "`/generate_recipes`   :    generates recipes based on items in virtual pantry.\n"
    #@data_str = data_str + spacer + "                      :    option <str>- filters used to generate specifi type of recipe." + "\n"  
    data_str = data_str + spacer + "`/show_pantry`        :    showing items in pantry.\n"
    data_str = data_str + spacer + "`/add_reciept`        :    processes receipt. updates items into virtual pantry.\n"
    data_str = data_str + spacer + "`/help`               :    shows commands\n"


    page_help = interactions.Embed(title = title,description=data_str,color ="50776")
    await ctx.send(embeds=page_help)

#########################################################################

################## ADD RECEIPT ######################
@bot.command(

    name="add_receipt",
    description="Add image of receipt to be added to virtual pantry",
    options=[
                interactions.Option(
                    name="img_file",
                    description="image of receipt grocery store.",
                    type=interactions.OptionType.ATTACHMENT,
                    required=True,
                ),
            ]
)

async def add_receipt(ctx: interactions.CommandContext,img_file):
    file_name = img_file.filename
    await ctx.send("Registering image: {}".format(file_name))
    engine.register_receipt(img_file.url)

#########################################################

################### SHOW PANTRY #########################

@bot.command(

    name="show_pantry",
    description="Prints out all items in virtual pantry."
)


async def show_pantry(ctx: interactions.CommandContext):
    food_names = engine.get_food_items()
    title = "____| Pantry Items |____\n"

    #print(data)
    await ctx.send("`{}{}`".format(title,food_names))
############################################################


############# GENERATE RECIPE ###########################################
# components definitions
left_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="<",
    custom_id="left",
)

right_button = interactions.Button(
    style=interactions.ButtonStyle.DANGER,
    label=">",
    custom_id="right",
)
confirm_button = interactions.Button(
    style=interactions.ButtonStyle.SUCCESS,
    label="confirm",
    custom_id="confirm_recipe",
)
row = interactions.ActionRow(
    components=[left_button, right_button, confirm_button]
)
# component handlers
@bot.component("left")
async def left_button_response(ctx: interactions.ComponentContext):
    global current
    if current > 0:
        current -= 1
    await ctx.edit(embeds=bot.recipe_pages[current],components=row)

@bot.component("right")
async def right_button_response(ctx: interactions.ComponentContext):
    global current

    if current < len(bot.recipe_pages) - 1:
        current += 1

    await ctx.edit(embeds=bot.recipe_pages[current],components=row)

@bot.component("confirm_recipe")
async def confirm_button_response(ctx: interactions.ComponentContext):
    global current
    await ctx.send(embeds=bot.ingredient_list[current],components=recipe_info_row)

def get_interactions_options(search_type):
    generate_recipe_options = []
    dict_options = {}
    for key,value in engine.recipe.spoonacular_info[search_type]["options"].items():
        required_info = bool()
        if(key == "required"):
            required_info = True
        elif(key == "optional"):
            required_info = False

        for recipe_command,type_option in value.items():
            type_interactions = get_type_interaction(type_option)
            options_interaction = interactions.Option(
                #HACK: apparently options name has to be lowercase
                            name=recipe_command.lower(),
                            description="filter: {} for generation of recipes.".format(recipe_command),
                            type=type_interactions,
                            required=required_info
                        )

            generate_recipe_options.append(options_interaction)

    return generate_recipe_options



@bot.command(
    name="generate_recipe",
    description="generates recipes",
    options=get_interactions_options("complexSearch")
)

#TODO: add option for number of recipes to generate

async def generate_recipe(ctx,*args,**kwargs):
    page_list = []
    instruction_list = []
    ingredient_list = []

    #
    food_names = engine.gen_recipe(kwargs)
    number_recipes_generated = len(food_names)

    no_recipe_found = interactions.Embed(title = "Recipe Info",description="No recipes found.",color ="50776")

    for number,data in enumerate(food_names,1):

        title,ingredient_str,instruction_str,page_str, image_url = engine.recipe.get_recipe_info(data)
        
        #creating pages of instruction and ingredients
        instructions_page = interactions.Embed(title = "{}: Instructions".format(title),description=instruction_str,color ="16745308")
        ingredients_page = interactions.Embed(title = "{}: Ingredients".format(title),description=ingredient_str,color ="16745308")  
        page = interactions.Embed(title = title,description=page_str,color ="50776",footer=interactions.EmbedFooter(text="Recipe #{}".format(number)))
        page.set_thumbnail(url=image_url)
        ingredients_page.set_thumbnail(url=image_url)
        instructions_page.set_thumbnail(url=image_url)

        page_list.append(page)
        instruction_list.append(instructions_page)
        ingredient_list.append(ingredients_page)

    bot.recipe_pages = page_list
    bot.instruction_list = instruction_list
    bot.ingredient_list = ingredient_list

    #handling num recipes specified 
    if(number_recipes_generated == 0):
        msg = await ctx.send(embeds=no_recipe_found,components=row)

    if(current > number_recipes_generated):
        msg = await ctx.send(embeds=bot.recipe_pages[number_recipes_generated],components=row)
    else:
        msg = await ctx.send(embeds=bot.recipe_pages[current],components=row)





# confirmed recipe components
ingredient_button = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="ingredients",
    custom_id="ingredients",
)

instruction_button = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="instructions",
    custom_id="instructions",
)

recipe_info_row = interactions.ActionRow(
    components=[ingredient_button,instruction_button]
)
@bot.component("ingredients")
async def ingredient_button_response(ctx: interactions.ComponentContext):
    global current
    await ctx.edit(embeds=bot.ingredient_list[current],components=recipe_info_row)

@bot.component("instructions")
async def instruction_button_response(ctx: interactions.ComponentContext):
    global current
    await ctx.edit(embeds=bot.instruction_list[current],components=recipe_info_row)
################################################################################


################ GET MONTHLY SPENDING ##################################

@bot.command(

    name="get_monthly_spending",
    description="Getting food spending total."
)
async def get_monthly_spending(ctx: interactions.CommandContext):
    total = engine.get_budget_items()
    data_str = "Total spending: {}".format(str(total))
    await ctx.send("`{}`".format(data_str))

#######################################################################


############### RETURNS LOG FILE INFO #################################
@bot.command(

    name="show_log",
    description="prints out log info."
)

async def show_log(ctx: interactions.CommandContext):
    log_info = engine.get_log_file_data()

    #print(data)
    embed = interactions.Embed(title="LOG INFO",description=log_info)
    await ctx.send(embeds=embed)

#######################################################################


bot.start()