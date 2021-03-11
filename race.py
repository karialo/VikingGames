#!/usr/bin/python3
# https://pastebin.com/pKTtgvYk

import random
import time
import os
	
	
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
		for i in range (random.randint(self.min, self.max)):
			self.position = self.position + character
		

def clear():
		os.system("cls")if os.name =="nt" else os.system("clear")

def update():
	clear()
	print(f"Round {round} / {rounds}.\n")
	print(f"({rabbit.score}) {rabbit.name:<6} - {len(rabbit.position):>3}% {rabbit.position}")
	print(f"({turtle.score}) {turtle.name:<6} - {len(turtle.position):>3}% {turtle.position}\n\n")
	time.sleep(0.2)
	
def reset():
	rabbit.position, turtle.position = "", ""
	rabbit.victory, turtle.victory = False, False
	
def scores():
	clear()
	print(f"{rabbit.name} has won {rabbit.score} races.")
	print(f"{turtle.name} has won {turtle.score} races.\n\n")
	if rabbit.score > turtle.score:
		print(f"{rabbit.name} has won the tournament!!")
	else:
		print(f"{turtle.name} has won the tournament!!")
	print("\n\n")

def add_point(x):
	x.score = x.score + 1

rabbit = Animal("Rabbit", 5, 7)# should be higher
turtle = Animal("Turtle", 1, 3)

def go():
	token = 1
	update()

	for i in range(3):
		rabbit.go()
		rabbit.go()
		turtle.go()
		update()
		time.sleep(0.2)
	
	while (turtle.victory == False) and (rabbit.victory == False):
		sleep_chance = random.randint(1,100)
		if sleep_chance > 80:
			rabbit.go()
			turtle.go()
		else:
			turtle.go()
		
		update()
		
		if (len(turtle.position) >= 100):
			add_point(turtle)
			input(f"Turtle wins round {round}.\n\n")
			break
		if (len(rabbit.position) >= 100):
			add_point(rabbit)
			input(f"Rabbit wins round {round}\n\n")
			break

clear()
round = 0
rounds = 9

for i in range (int(rounds)):
	round = round + 1
	reset()
	go()
	
reset()
update()
scores()
