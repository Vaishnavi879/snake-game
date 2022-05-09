from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        file=open("data.txt", mode='r')
        content=file.read()
        self.score=0
        self.high_score=int(content)
        file.close()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.scoring()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, "center", ("Courier", 24, "normal"))

    def scoring(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center",("Courier",24,"normal"))
        self.score+=1

    def reset(self):
        if(self.score>self.high_score):
            self.high_score=self.score
            file=open("data.txt", mode='w')
            file.write(str(self.high_score))
            file.close()
        self.score=0


