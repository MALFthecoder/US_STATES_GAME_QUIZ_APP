import turtle  #Import the `turtle` module for creating graphics.
import pandas  #import pandas

#TODO 1: Turtle and Screen Setup
screen = turtle.Screen() # Create a `turtle.Screen()` object.
turtle.title("U.S. 50 States Quiz Applications") #Set the screen title.
background_image = ("blank_states_img.gif") #Load the background image.
screen.addshape(background_image) #Add the background image to the screen

#TODO 2: CSV data handling ( Import pandas module for working with CSV data)
#TODO 3: Read the CSV file ("50_states.csv") using `pandas.read_csv()`.
#TODO 4: Data Lists
   #TODO 5:Create a list `all_states` containing all the state names from the CSV data.
   #TODO 6:Create an empty list `guessed_states` to keep track of correctly guessed states.


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = [] 

