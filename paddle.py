from turtle import Turtle
class Paddle(Turtle):
    def __init__(self , x_x , y_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5 , stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x= x_x, y = y_y)
        


    def up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor() , self.new_y)

    def down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor() , self.new_y)
        
            
            


        
    
