import turtle
import pandas

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.tracer(0)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Gets the coordinates of states
# def get_mouse_click_coordinate(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coordinate)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
screen.update()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
guessed_state = []

while len(guessed_state) < 50:
    screen.update()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(arg=answer_state, font=FONT)
        guessed_state.append(answer_state)
        screen.update()

    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state name?").title()
