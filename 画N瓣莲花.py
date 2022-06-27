import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.pencolor("gold")
n=int(turtle.numinput("How many leaf of lotous you want to draw?", 3))

def draw_leaf():
   for i in range(2):
      t.circle(210,720/n)  # 画圆弧，半径，弧的角度
      t.lt(180-360/n)   # 画完一次弧后，画笔转的角度
      
     
for i in range(n):
    t.width(2)
    draw_leaf()
    t.rt(360/n)

    
