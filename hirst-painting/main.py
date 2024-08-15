import random
from turtle import Turtle, Screen, colormode
# import colorgram
#
# # Extracting the colors and creating a color palette
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# # Creating a list of tuples for the RGB proportion of colors present.
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Extracted all the colors and got rid of the background white color.
color_list = [(202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124),
              (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41),
              (147, 178, 147), (163, 142, 156), (234, 177, 165), (55, 46, 50), (130, 28, 31), (184, 205, 174),
              (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63),
              (175, 192, 212)]

colormode(255)

# Created a turtle and assigned its position according to the image.
tim = Turtle()
tim.shape("classic")
tim.speed("fastest")
start_position = -350
tim.teleport(-380, start_position)
tim.penup()
tim.hideturtle()

# Loop for printing dots like the Hirst painting.
for _ in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(80)
    start_position = start_position + 80
    tim.teleport(-380, start_position)

# Exits when screen is clicked.
screen = Screen()
screen.exitonclick()
