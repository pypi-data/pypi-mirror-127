#!/usr/bin/env python

from MainGame import *
import random
import time

class Game1(WoG):
    def generate(self):
        self.res = random.sample(range(1, 101), self.Difficulty)
        res_str = f"Random number list is {self.res}"
        print(res_str, flush=True, end='\r')
        time.sleep(0.7)
        print('    ' * len(res_str))

    def get_input_from_user(self):
        try:    # must be a try with except because list doesn't support isdigit...
            self.user_res = list(map(int, input('Guess the generated list: ').split()))
        except ValueError:
            print('input is invalid')
            return self.get_input_from_user()


    def compare_results(self):
        i = 1
        while i < 3:  # the user gets 3 tries
            if self.user_res != self.res:
                print('The number you guessed is incorrect')
                i += 1
                self.get_input_from_user()
            else:
                print(f'Congrats, You made it! Generated list was {self.res}!')
                break

