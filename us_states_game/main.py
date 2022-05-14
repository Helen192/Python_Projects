import turtle
import pandas as pd
dataset = pd.read_csv('50_states.csv')
print(dataset)



screen = turtle.Screen()
screen.title("U.S. States Game")
# path to the image
image = "blank_states_img.gif"
#load the image to the screen
screen.addshape(image)
turtle.shape(image)

# setting the turtle which will write states on the screen
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()

score = 0
corrected_guess_list = []
# convert the data of state column into a list
state_list = dataset.state.to_list()

##TODO: Use a loop to allow the usere to keep guessing
while len(corrected_guess_list) < 50:
    ##TODO: Convert the guess to Title case
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    ##TODO: Check if the guess is among the 50 states

    if answer_state in state_list:
        row_state = dataset[dataset.state == answer_state]
        write_state.goto(int(row_state['x']), int(row_state['y']))
        ##TODO: Write correct guesses onto the map
        write_state.write(answer_state, align="center", font=("Arial", 12, "normal"))
        ##TODO: Keep track of the score
        score += 1
        ##TODO: Record the correct guesses in a list
        corrected_guess_list.append(answer_state)

    # check if user want to exit the game
    if answer_state == "Exit":
        ##TODO: save missing states to a file.csv
        missing_states = [state for state in state_list if state not in corrected_guess_list]
        #missing_states = []
        #for state in state_list:
        #    if state not in corrected_guess_list:
        #        missing_states.append(state)

        states_to_learn = {
            "Missing States": missing_states
        }
        pd.DataFrame(states_to_learn).to_csv("Missing States.csv")
        break


























