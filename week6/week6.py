# import turtle
# from configparser import LegacyInterpolation
#
# #--setup--
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
#
# tess=turtle.Turtle()
#
# #--functions--
#
# def drawPoly(someturtle, somesides, somesize):
#     angle = 360 /somesides
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.left(angle)
#
# def drawspiral(someturtle, angle):
#     size=1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size=size+2
#
# def drawEquitriangle(someturtle, somesize):
#     drawPoly(someturtle, 3, somesize)
#
# def drawStar(someturtle, size):
#    for i in range(5):
#         someturtle.forward(size)
#         someturtle.left(144)
#
# def drawSprite(someturtle, Legs, length):
#     angle=360/Legs
#     for i in range(Legs):
#         someturtle.forward(length)
#         someturtle.back(length)
#         someturtle.left(angle)
#
#
#
# #--exercises--
# # exercise 1
# # tess.pensize(3)
# # tess.color("hotpink")
# # drawPoly(tess, 8, 50)
#
# #exercise 2
# # tess.pensize(3)
# # tess.pencolor("blue")
# # for i in range(20):
# #     drawPoly(tess,4, 100)
# #     tess.left(18)
#
#
# #exercise 3
# # tess.pencolor("red")
# # tess.penup()
# # tess.goto(-150, 0)
# # tess.pendown()
# # drawspiral(tess,90)
# #
# # tess.penup()
# # tess.goto(150, 0)
# # tess.pendown()
# # drawspiral(tess,89)
#
# #exercise 4
# # tess.pensize(3)
# # tess.color("red")
# # tess.pencolor("red")
# # drawEquitriangle(tess, 100)
# #exercise 5
# # tess.color("red")
# # for i in range(5):
# #     drawStar(tess, 50)
# #     tess.penup()
# #     tess.forward(200)
# #     tess.right(144)
# #     tess.pendown()
# #exercise 6
#
# drawSprite(tess, 15, 120)
# # --finish--
#
# wn.exitonclick()