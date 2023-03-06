from treelib import Node, Tree
tree = Tree()
new_tree = Tree()
BASE_LAYER = 1
API_LAYER = 2
PROJECT_LAYER = 3
new_tree.create_node("python", BASE_LAYER)  # root node
"""
Setting up structure

python 
    __ API
    __ Projects
        __API_USED 

"""
new_tree.create_node("api", API_LAYER, parent=BASE_LAYER)
new_tree.create_node("projects", PROJECT_LAYER, parent=BASE_LAYER)

# Projects contents
# TODO: use repo name to locate start of proj
new_tree.create_node("discord", "discord", parent=PROJECT_LAYER)
# discord contents

#TODO automate this
"""
Create a hadnler to easily create this treeelib pattern so you can 
have an object to work with (easily call to parent-child ...) 
+ have access to object methods.
"""

# all items in lib
# aLL items in api class



new_tree.create_node("Plugins", "discord_plugins", parent="discord")
new_tree.create_node("APIs", "discord_apis", parent="discord")



new_tree.create_node("recipe", "recipe", parent="discord_plugins")
new_tree.create_node("entertainment", "entertainment", parent="discord_plugins")
new_tree.create_node("gym", "gym", parent="discord_plugins")
new_tree.create_node("receipt_ocr", "receipt_ocr", parent="discord_plugins")
new_tree.create_node("amazon", "amazon_discord", parent="discord_apis")
new_tree.create_node("discord_data_class", "discord_data_class_discord", parent="discord_apis")

# new_tree.create_node("recipe", "recipe", parent="discord")

"""
test dictionary

*any key with a value of an empty dictionary {} 
will hold the context in <key>.rst file*

index_struct = {
        "discord": {
            "plugins": {
                "recipe": {},
                "entertainment": {},
                "gym": {},
                "receipt_ocr": {},
                "discord_data_class": {},
                "amazon": {}
            },
            "apis": {
                "amazon": {},
                "discord_data_class": {}
            }
        }
    }
"""





# api Contents
new_tree.create_node("amazon", "amazon", parent=API_LAYER)
new_tree.create_node("discord_data_class", "discord_data_class", parent=API_LAYER)




#TODO: create method that takes dictionary to auto create nodes instead 
# of hardcoding
def create_rst(file_name, rst_structure, path="."):
    """ creates a rst file
    :param file_name: name of rst file to be generated
    :type file_name: <str>
    :param file_name: name of rst file to be generated
    :type file_name: <str>

    :return: rst file
    
    """
    rst_str = ""
    file_path = "{}/{}.rst".format(path, file_name)
    for title, list_items in rst_structure.items():
        print(list_items)
        rst_str += "{0}\n{1}\n\n".format(title, "="*len(title))
        rst_str += ".. toctree::\n"
        for item in list_items:
            rst_str += "\t{}\n".format(item.tag)
        rst_str += "\n"

    with open(file_path, "w") as rst_file:
        rst_file.write(rst_str)
        rst_file.close()
    
# layer = BASE_LAYER
# while(True):
#     children_l = new_tree.children(layer)
#     if (len(children_l) == 0):
#         break
#     else:
#         layer = 

# if new_tree.children(BASE_LAYER):
#     if()

# creating 
# calling to new_tree object in order to get structure 
# (parent child relationship) shown below
sphinx_titles = {
    "API": new_tree.children(API_LAYER),
    "Projects": new_tree.children(PROJECT_LAYER)
}
create_rst(new_tree.__getitem__(BASE_LAYER).tag, sphinx_titles)


# create project rst file 
for project_item in new_tree.children(PROJECT_LAYER):
    sphinx_titles = {
        "Plugins": new_tree.children("discord_plugins"),
        "APIs Used": new_tree.children("discord_api")
    }    
    create_rst(project_item.tag, sphinx_titles)

# Creating rst for API
# sphinx_titles = {
#     "API": new_tree.children(API_LAYER)
# }    
# create_rst("api", sphinx_titles)

# creating rst for Project
# sphinx_titles = {
#     "Projects": new_tree.children(PROJECT_LAYER)
# }    
# create_rst("projects", sphinx_titles)


print(new_tree.__getitem__(API_LAYER))
new_tree.show()