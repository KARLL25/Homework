import turtle as t
t.speed(0)
t.pensize(3)

def shape(size,sides):
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)

for j in range(12):
    for colours in ['violet','blue',"green","yellow","pink","brown"]:
        for i in range(12):
            t.color(colours)
            shape(20,3)
            t.forward(10)
            t.left(5)
    t.penup()
    t.forward(20)
    t.right(30)
    t.pendown()
t.exitonclick()
