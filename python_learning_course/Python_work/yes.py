#password_generator:

import random
import pandas as pd

class password_generator():
    def __init__(self):
        super().__init__()
        #print('This is your password')
        self.x = self.jon()
        print(self.stringify())


    def word_generator(self):
        self.alpha = 'abcdefghijklmnopqrstuvwxyz'
        self.upper = self.alpha.upper()

        self.toge = self.alpha+self.upper
        return sorted([random.choice(self.toge) for x in range(7)])

    def sym_gen(self):
        self.sym ='@#$%*&!_-()'
        return  sorted([random.choice(self.sym) for x in range(random.choice([1,2,3]))])

    def jon(self):
        return [''.join(x) for x in self.word_generator()+self.sym_gen()]


    def stringify(self):
        self.pass_gen =''
        for i in self.x:
            self.pass_gen += i
    

        return self.pass_gen

w = [password_generator() for x in range(100)]



