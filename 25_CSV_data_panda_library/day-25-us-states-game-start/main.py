import turtle
import pandas

screen=turtle.Screen()
screen.title("US STATE NAME QUIZ")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state)<50:
    answer_guess=screen.textinput(title=f"{len(guessed_state)}/50GUESS THE STATE",prompt="enter your Guess:").title()
    if answer_guess=="Exit":
        missing_state=[states for states in all_states if states not in guessed_state]
        # missing_state=[]
        # for states in all_states:
        #     if states not in guessed_state:
        #         missing_state.append(states)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_remember.csv")
        break
    
    if answer_guess in all_states:
        guessed_state.append(answer_guess)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_guess]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_guess)
        print(f"answer available {answer_guess}.")
