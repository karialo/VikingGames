# coding: utf-8
import random
# from race import update


class Animal:
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max
        self.position = ""
        self.score = 0
        self.victory = False

    def go(self):
        character = "|"
        for i in range(random.randint(self.min, self.max)):
            if len(self.position) != 100:
                self.position = self.position + character
