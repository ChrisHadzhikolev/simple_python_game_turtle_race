from turtle import Turtle, Screen
import random as rand

racers = []
colors = ("red", "green", "blue", "yellow", "purple", "black")

starting_y_pos = 214
for turtle_id in range(0, 6):
    racer = Turtle(shape="turtle")
    racer.color(colors[turtle_id])
    racer.penup()
    racer.goto(-285, starting_y_pos-50)
    starting_y_pos -= 50
    racers.append(racer)

screen = Screen()
screen.setup(height=600, width=600)

def random_pace():
    return rand.randint(1, 10)


def start_race():
    race_over = False
    user_bet = screen.textinput(title="Make a Bet", prompt=f"Choose color from {colors}")
    while not race_over:
        for turtle in racers:
            if turtle.xcor() > 280:
                race_over = True
                if user_bet == turtle.pencolor():
                    print("you guessed correct")
                else:
                    print(f"wrong guess, {turtle.pencolor()} wins")
            turtle.forward(random_pace())


start_race()
screen.exitonclick()
