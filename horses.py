#!/usr/bin/python3

import random
import time
import os

horse_names = [	"Purple rain", "Seattle Slew", "Man o' War", "Citation", "Red Rum",
    			"Seabiscuit", "Kelso", "Lady LaRoux", "Daddy's Girl" ]

colours, horses = [], []
line = ("-"*22 ) + "||" + ("-" * 101) + "||"
end = False
gg = '~\u2588\u2588=o'


class Player:
	def __init__(self):
		self.balance = 100


class Ui:
	def clear():
		os.system("cls")if os.name =="nt" else os.system("clear")

	def update():
		Ui.clear()
		print(f"\033[1;37;40m                              Race {round} / {rounds}.")
		for i in horses:
			print(f"{line}\n{i.colour}({i.score}) {i.name:<13} {i.pos:<3}\033[1;37;40m{i.colour}{' '*i.pos}{gg} \033[1;37;40m")
		print(line)


class Game:
	def creation(number):
		col = 31
		for i in zip(range(int(number)), horse_names):
			col = col + 1
			horses.append(Animal(str(i[1]), 1, 3, "\033[1;" + str(col) + ";40m"))
	
	def reset():
		for i in horses:
			i.pos = 0
			i.victory = False
	
	def scores():
		Ui.clear()
		for horse in horses:
			print(f"{horse.name} has won {horse.score} races.")

	def add_pt(x):
		x.score = x.score + 1
		

class Animal:
	def __init__(self, name, min, max, colour):
		self.name = name
		self.colour = colour
		self.min = min
		self.max = max
		self.pos = ""
		self.score = 0
		self.victory = False
		
	def go(self):
		token = 1
		for i in range (random.randint(self.min, self.max)):
			self.pos = self.pos + token


round = 0
rounds = 1

Ui.clear()
rounds = input("How many races?: ")
Game.creation(input("How many horses will race? (1 - 9) "))
player = Player()
Game.reset()

for i in range (int(rounds)):
	round = round + 1
	end = False
	Game.reset()
	Ui.update()
	time.sleep(1)
	while end == False:
		Ui.update()
		time.sleep(0.2)
		for horse in horses:
			horse.go()
			if horse.victory == False:
				if (horse.pos >= 100):
					horse.pos = 100
					Ui.update()
					horse.victory = True
					end = True
					Game.add_pt(horse)
					print(f"\nWinner: {horse.name}")
					time.sleep(3)
					break

Game.scores()
