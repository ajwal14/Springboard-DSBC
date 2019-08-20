import random

class Coin:
    def __init__(slef, rare=False,clean=True):
        self.is_rare = rare
        self.is.clean = clean

        if self.is_rare:
            self.value = self.orginal_value * 1.25
        else:
            self.value = self.orginal_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

class Pound:

    def __init__(self,rare=False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

    def rust(self):
        self.color = "greenish"


    def clean(self):
        self.color = "gold"


    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin Spent")
