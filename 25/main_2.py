import turtle
import pandas

def get_mouse_click_coor(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("U.s STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the state", prompt="What's the name of the state")

pandas.read_csv("50_states.csv")

