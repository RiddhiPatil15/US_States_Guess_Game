import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is the name of the state?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
