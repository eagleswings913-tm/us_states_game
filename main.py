
import turtle
import pandas
import tkinter
from stylus import Stylus

screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
pencil = Stylus()

# def get_coordinates(x,y):
#     print(f'You clicked at coordinates: ({x},{y})')
#
# turtle.onscreenclick(get_coordinates, 1)

states_data = pandas.read_csv('50_states.csv')
states = states_data['state'].tolist()
guessed_states = []
coordinates_list = list(zip(states_data['x'], states_data['y']))

number_correct = 0
game_on = True
while game_on:
    if number_correct < 50:
        while True:
            answer_state = screen.textinput(title=f" {number_correct} / 50 correct", prompt="Guess a State - Enter a state name: ")
            if answer_state.title() not in states and answer_state != "q":
                tkinter.messagebox.showinfo("Guess a State", "Not a valid state name! Try again")
            elif answer_state.title() in guessed_states:
                tkinter.messagebox.showinfo("Guess a State", f"{answer_state.title()} was already guessed, Try a different state!")
            else:
                break
        if answer_state.title() == "Q":
            game_on = False
            tkinter.messagebox.showinfo("Guess a State", "Game Over!  Try again later")
        else:
            number_correct += 1
            state_index = states.index(answer_state.title())
            guessed_states.append(states[state_index])
            coordinates = coordinates_list[state_index]
            pencil.write_state_name(answer_state.title(), coordinates)
    else:
        game_on = False
        tkinter.messagebox.showinfo("Guess a State", "You got all 50 states! Well done!")

turtle.listen()
turtle.mainloop()
