import turtle
import pandas

screen = turtle.Screen()
screen.title = "U.S. States Game"
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guess = 0

data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
guessed_states = []


while len(guessed_states) != 50:
    answer_state = (screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name?")).title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        correct_guess += 1
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
