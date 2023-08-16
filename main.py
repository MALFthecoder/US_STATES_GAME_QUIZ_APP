import turtle
import pandas

screen = turtle.Screen()
turtle.title("U.S. 50 States Quiz Applications")
background_image = ("blank_states_img.gif")
screen.addshape(background_image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


turtle.shape(background_image)




turtle.mainloop()
