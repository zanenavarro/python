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


class entertainment(Util):
    def __init__(self):


    ############ FINDING SHOW, MOVIES #######################

    def find_show(search_word):
        results_info = {}
        results_info["netflix"] = netflix_search(search_word)
        results_info["youtube"] = youtube_search(search_word)
        results_info["amazon_prime"] = amazon_prime_search(search_word)
        results_info["hbo_max"] = hbo_max_search(search_word)
        results_info["peacock"] = peacock_search(search_word)


        
    
    def netflix_search(self,search_word):
        print_debug("searching netflix...")
    
    def youtube_search(self,search_word):
        print_debug("searching youtube..")

    def amazon_prime_search(self,search_word):
        print_debug("searching amazin prime...")
    
    def hbo_max_search(self,search_word):
        print_debug("searching hbo max...")

    def peacock_search(self,search_word)
        print_debug("searching for peacock...")











    ##########################################################
