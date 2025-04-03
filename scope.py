from turtle import Turtle

# this class responsible for creating the game field
class Scope(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(350, -200)
        self.pendown()
        for i in range(1, 5):
            self.left(90)
            self.forward (700) if (i % 2 == 0) else self.forward (400)

# this class is responsible for creating the game's instructions
class Instructions(Turtle):
    def __init__(self):
        super().__init__()
        self.display_instructions()

    def display_instructions(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-30, 120)
        self.write("Instructions: \n", align='center', font=('Arial', 16, 'bold'))
        self.color("#00FFFF")
        self.goto(-20, 90)
        self.write(" Controls: \n", align='center', font=('Arial', 14, 'normal'))
        self.color("#00FFFF")
        self.goto(0, 80)
        self.write("   - Left/Right Arrows: Move the bar", font=('Arial', 12, 'italic'))
        self.color("#00FF00")
        self.goto(-20, 30)
        self.write("Scoring: \n", align='center', font=('Arial', 14, 'normal'))
        self.color("#FFD700")
        self.goto(0, 10)
        self.write("   - Turtle (non-white): +5 points\n", font=('Arial', 12, 'italic'))
        self.color("#FFD700")
        self.goto(0, -20)
        self.write("   - Square: +2 points\n", font=('Arial', 12, 'italic'))
        self.color("#FFD700")
        self.goto(0, -50)
        self.write("   - Circle OR Arrow: +1 point\n", font=('Arial', 12, 'italic'))
        self.color("#FFD700")
        self.goto(0, -80)
        self.write("   - Triangle OR Classic shape will reset your score to 0\n", font=('Arial', 12, 'italic'))
        self.color("#FF6347")
        self.goto(0, -100)
        self.write("Press ENTER to start the game", align='center', font=('Arial', 16, 'bold'))
