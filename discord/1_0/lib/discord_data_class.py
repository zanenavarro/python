import json
import sys
sys.path.append("../../util")
from Util import Util         

# testing sphinx gen yml         
 
class discord_data_class(Util):

    def __init__(self):
        super(discord_data_class).__init__()
        self.embed_list = []
        # self.body_type = {
        #     # "PONG": 1,
        #     # "CHANNEL_MESSAGE_WITH_SOURCE": 4,
        #     # "DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE": 5,
        #     # "DEFERRED_UPDATE_MESSAGE": 6,
        #     # "UPDATE_MESSAGE": 7,
        #     # "APPLICATION_COMMAND_AUTOCOMPLETE_RESULT": 8,
        #     # "MODAL": 9
        # }
        # TODO: discord_lib to hold items 

        self.discord_message = {
            "tts": False,
            "content": "",
            "embeds": [],
            "allowed_mentions": {
                    "parse": []
                },
            "flags": 0,
            "components": [],
            "attachments": [],
        }

        # https://discord.com/developers/docs/resources/channel#embed-object
        self.embed_dict = {
            "title": "",
            "type": "",
            "description": "",
            "url": "",
            "color": 0,
        }
        self.embed_image_structure = {

            "url": "",
            "prox_url": "",
            "height": "",
            "width": ""

        }
        self.title_name = "NOT_DEFINED"

    def set_embed_description(self, description_info):
        """ sets embed description
        :param: description_info: description str to be used in embed 
        :type: description_info: <str>
        :return: None
        :return: type
        """
        self.embed_description = description_info

    def load_embed_content(self):
        """create array of embeds
        :param: content_list: list of message content
        :type: content_list: <list>
        :return: None
        """

        # Get embed template
        temp_dict = self.embed_dict.copy()
        
        # Add items       
        temp_dict["description"] = self.embed_description
        temp_dict["title"] = self.title_name
        
        # Updates global embed list
        self.embed_list.append(temp_dict)

    def get_message(self, type_num):
        # Default to only embeds
        """returns a discord message
        :param: type: body type of message
        :type: type: <str>
        :return: message_data: discord interaction object
        :rtype: <dict>
        """
        self.discord_message["embeds"] = self.embed_list
        self.embed_list = []
        message_data = {
                'statusCode': 200,
                'body': {
                    'type': type_num,
                    'data': self.discord_message
                    }
                }
        return message_data

    def set_embed_title(self, title_name):
        """ Sets title of discord embed
        :param: title_name: title of embed
        :type: title_name: <str>
        :return: None
        """
        self.title_name = title_name

    def set_embed_image(self, image_url, height, width, proxy_url=None):
        """ Sets title of discord embed
        :param: image_url: title of embed
        :type: image_url: <str>
        :param: height: height of image
        :type: height: <str>
        :param: width: width of image
        :type: width: <str>
        :param: proxy_url: proxy_url
        :type: proxy_url: <str>
        :return: None
        """
        embed_image = self.embed_image_structure.copy()
        embed_image["url"] = image_url
        embed_image["proxy_url"] = proxy_url
        embed_image["height"] = height
        embed_image["width"] = width
        self.image = embed_image

    def get_embed_image(self):
        """ retrieves embed image object
        :return: embed image object
        :rtype: <dict>
        """
        return self.image

    def set_embed_color(self, color):
        """ Sets color for discord embed
        :param: color: color of discord embed
        :type: color: <int>
        :return: None
        """
        self.color = color
