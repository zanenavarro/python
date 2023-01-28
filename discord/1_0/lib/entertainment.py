"""
ENVISION:

a class thaf has methods to search movies and shows for every provider

method 1) find_show (search_word)
returns
  - Netlfix api
  - Hulu api
  - youtube api
  - peacock api
  - amazon prime video
  - etc


"""
from ..util import AmazonHelper
from discord_data_class import discord_data_class



class EntertainmentHelper(AmazonHelper):
    def __init__(self):
        super(EntertainmentHelper).__init__()
        self.discord_data_class = discord_data_class()


    ############ FINDING SHOW, MOVIES #######################

    def find_show(self, search_word):
        results_info = {}
        results_info["netflix"] = self.netflix_search(search_word)
        results_info["youtube"] = self.youtube_search(search_word)
        results_info["amazon_prime"] = self.amazon_prime_search(search_word)
        results_info["hbo_max"] = self.hbo_max_search(search_word)
        results_info["peacock"] = self.peacock_search(search_word)


        
    
    def netflix_search(self,search_word):
        self.print_debug("searching netflix...")
    
    def youtube_search(self,search_word):
        self.print_debug("searching youtube..")

    def amazon_prime_search(self,search_word):
        self.print_debug("searching amazin prime...")
    
    def hbo_max_search(self,search_word):
        self.print_debug("searching hbo max...")

    def peacock_search(self,search_word)
        self.print_debug("searching for peacock...")











    ##########################################################
