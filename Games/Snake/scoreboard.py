from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # self.highscore = 0
        with open('score_log.txt') as data:
            self. highscore = int(data.read())

        self.hideturtle()
        self.color("White")
        self.penup()
        self.score_level = " "
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.score_level == "easy":
            text_col = "green"
        elif self.score_level == "medium":
            text_col = "blue"
        elif self.score_level == "hard":
            text_col = "red"
        else:
            text_col = "black"
        self.goto(0, 270)
        self.color("White")
        # self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align="center", font=("Arial", 12, "normal"))
        self.goto(-270, 270)
        self.color(text_col)
        self.write(f"Level: {self.score_level}", align="left", font=("Courier", 12, "normal"))
        # print(f"Level in Score {self.score_level}") # Debugging
        # self.write(f"Highscore: {self.highscore}", align="right", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER ☠️ !!", align="center", font=("Courier", 12, "normal"))
    def dead_snake(self):
        self.goto(0, 0)
        self.color('white')
        self.write("You died ☠️ !!", align="center", font=("Courier", 12, "normal"))
    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            # saving highscore in file
            with open('score_log.txt',mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

