import another_module

print(another_module.another_variable)


from turtle import Turtle,Screen

jimmy = Turtle()

# print(jimmy)
# jimmy = turtle.Turtle()
# the shape() are methods defined in turtle 
jimmy.shape("turtle")
jimmy.color("coral")
jimmy.forward(100)
jimmy.left(120)
jimmy.forward(100)
jimmy.left(120)
jimmy.forward(100)
jimmy.left(120)
jimmy.home()


# this part make the screen, all the turtle will be shown in this screen
# until then next piece of instruction will be executed
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()