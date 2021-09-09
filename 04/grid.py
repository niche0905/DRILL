import turtle

count = 0
turtle.penup()
while (count < 6):
    turtle.goto(0, count * 100)
    turtle.pendown()
    turtle.goto(500, count * 100)
    turtle.penup()
    count += 1

count = 0
turtle.penup()
while (count < 6):
    turtle.goto(count * 100, 0)
    turtle.pendown()
    turtle.goto(count * 100, 500)
    turtle.penup()
    count += 1

turtle.exitonclick()
