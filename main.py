import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                    prompt='What\'s another state\'s name?').title()
    if answer_state in all_states:
        if answer_state in guessed_states:
            print(f'You\'ve already guessed {answer_state}!')
            continue
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer_state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(f'{answer_state}')

        guessed_states.append(answer_state)
    elif answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv('states_to_learn.csv')
        break
    else:
        print(f'{answer_state} is not a correct state.')
