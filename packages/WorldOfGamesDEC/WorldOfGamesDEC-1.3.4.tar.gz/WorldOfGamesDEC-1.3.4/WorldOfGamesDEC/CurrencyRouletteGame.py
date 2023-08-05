#!/usr/bin/env python

from MainGame import *
import random
import requests
import json

class Game3(WoG):
    def generate(self):
        url = "https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=ultra&apiKey=3eee6e211600d6203628" #  the free API
        res = requests.get(url)
        if res.status_code != 200:
            return -1
        else:
            data = res.text
            parsed = json.loads(data)
            self.USD_ILS = float(parsed["USD_ILS"])     #get the value
            self.random_number = random.randint(1, 101)     #generate random number
            print(f'{self.random_number} USD')
            self.gen_number = round(self.random_number//self.USD_ILS)     # round it to integer
            self.gen_list = list(range(self.gen_number-self.Difficulty, self.gen_number+self.Difficulty)) #generate a list in the range of difficulty
            #print(f'{self.gen_list}') #Delete the sharp symbol when you want to test

    def get_input_from_user(self):
        self.User_Guess = int(input(f'Guess the number in ILS: '))

    def compare_results(self):
        i = 1
        while i < 3:  # the user gets 3 tries
            if self.User_Guess not in self.gen_list:
                print('The number you guessed is incorrect')
                i += 1
                self.get_input_from_user()
            else:
                print(f'Congrats, You made it! Generated number was {self.gen_number}!')
                break




