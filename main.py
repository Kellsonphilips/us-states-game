
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states = pandas.read_csv("50_states.csv")
states = all_states.state.to_list()

user_guess_answer = []

while len(user_guess_answer) < 50:
    user_state_guess = screen.textinput(title=f"{len(user_guess_answer)}/50 States Correct",
                                        prompt="What is another state name?").title()

    if user_state_guess == "Exit":
        # using 1 line of code list comprehension to replace 4 lines with a loop
        missed_states = [state for state in states if state not in user_guess_answer]
        # missed_states = []
        # for state in states:
        #     if state not in user_guess_answer:
        #         missed_states.append(state)
        list_of_missed_state = pandas.DataFrame(missed_states)
        list_of_missed_state.to_csv("missed_states_learn.csv")
        break
    if user_state_guess in states:
        user_guess_answer.append(user_state_guess)
        word = turtle.Turtle()
        word.penup()
        word.hideturtle()
        match_state = all_states[all_states.state == user_state_guess]
        x_axis = int(match_state.x)
        y_axis = int(match_state.y)
        word.goto(x_axis, y_axis)
        word.write(user_state_guess, False, align="left", font=("Arial", 10, "normal"))

# # filtering the guessed states and the left state
# missed_states = list(set(states) - set(user_guess_answer))
# print(missed_states)
# print(len(missed_states))
#
# missed = pandas.DataFrame(missed_states)
# missed.to_csv("missed_states.cvs")
