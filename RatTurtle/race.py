#!/usr/bin/python3
# https://pastebin.com/pKTtgvYk
import random
import time
import os
from animal import Animal


def clear():
    # clear the terminal screen
    os.system('cls') if os.name == 'nt' else os.system('clear')


def update():
    clear()
    print(f"Round {curr_round} / {total_round}.\n")
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


rabbit = Animal("Rabbit", 5, 7)  # should be higher
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
        sleep_chance = random.randint(1, 100)
        if sleep_chance > 20:
            # rabbit doesn't sleep
            rabbit.go()
            turtle.go()
            time.sleep(0.01)
            update()
        else:
            for i in range(random.randint(20, 40)):
                turtle.go()
                time.sleep(0.01)
                update()
                if len(turtle.position) >= 100:
                    turtle.position = "|" * 100
                    update()
                    break

        if len(turtle.position) >= 100:
            turtle.position = "|" * 100
            update()
            add_point(turtle)
            input(f"Turtle wins round {curr_round}.\n\n")
            break

        if len(rabbit.position) >= 100:
            rabbit.position = "|" * 100
            update()
            add_point(rabbit)
            input(f"Rabbit wins round {curr_round}\n\n")
            break


if __name__ == '__main__':
    clear()
    curr_round = 0  # current round

    total_round = 9

    # 2021-04-16 jet
    for _ in range(total_round):
        curr_round += 1
        reset()
        go()

    reset()
    update()
    scores()
