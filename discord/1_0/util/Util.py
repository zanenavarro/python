import json
import datetime


class Util():

    def __init__(self):
        self.debug = True
        self.create_log_file()

    def get_dictionary(self, path_to_json):
        """ Gets dictionary from JSON file
        :param: path_to_json: path to JSON file
        :type: path_to_json: <str>
        :return: data: Dictionary extracted from JSON file
        :rtype: data: <str>
        """
        data = {}
        with open(path_to_json, "r") as json_file:
            data = json.load(json_file)
        return data

    def print_debug(self, message):
        """ Prints message
        :param: message: Message to print
        :type: message: <str>
        :return: None
        """
        date = datetime.datetime()
        today = date.now()
        date_str = today.strftime("%c")

        if (self.debug):
            print(message)
            with (open("discord.log"), 'a') as file:
                file.write("{}: discord_bot: {}".format(date_str, message))
                file.close()

    def print_dictionary(self, path, data, character):
        """Prints dictionary to JSON file
        :param: path: path to JSON file
        :type: path: <str>
        :param: data: dictionary to print
        :type: data: <dict>
        :param: character: werite character
        :type: character: <str>
        :return: None
        """
        with open(path, character) as json_file:
            json.dump(data, json_file, indent=4)
            json_file.close()

    def create_log_file(self):
        """ Creates a log file
        :return: None
        """
        log_str = ""
        with open("discord.log", "w") as log_file:
            log_file.write(log_str)
            log_file.close()

    def get_log_file_data(self):
        """ Gets log file data
        :return: data_str: Returns log file information
        :rtype: data_str: <str>
        """
        data_str = ""
        with open("discord.log", "r") as log_file:
            data_str = log_file.read()
            log_file.close()

        return data_str
