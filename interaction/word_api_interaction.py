import requests, json
import random

class word_api_manipulator():
    
    def __init__(self):
        self.base_url = "https://wordle-api.cyclic.app/words" # defines the api url
    
    def get_word(self):
        response = requests.get(self.base_url) #utilises requests function to fetch api data from the given url and assign it to the response variable
        
        if response.status_code == 200: # ensures api can be accessed through its response code, using the .status_code function in requests
            word_list = response.json() # creates a list of the data returned from the response variable
            random_word = random.choice(word_list) # gets a random word from word_list
            return (random_word['word']) # returns a random word from the word_list, eliminating the further url attacthed to each word
        else:
            return None
