import random


class Game:
    def __init__(self) -> None:
        self.winning_no = random.randint(a+1, b-1)
        self.chance_took = 1

    def play(self):
        guess = int(input(f"please guess a no between {a} and {b}\n"))
        while guess != self.winning_no:
            if guess > self.winning_no:
                guess = int(input("wrong guess enter a smaller no. again\n"))
            else:
                guess = int(input("wrong guess enter a greater no. again\n"))
            self.chance_took += 1
        print(f"Correct you took {self.chance_took} trials to guess the number")


a = int(input("enter the value of a="))
b = int(input("enter the value of b="))
player1 = Game()
player2 = Game()
print("player 1:")
player1.play()
print("player 2:")
player2.play()
if player1.chance_took > player2.chance_took:
    print("Player 2 wins!")
elif player2.chance_took > player1.chance_took:
    print("Player 1 wins!")
else:
    print("Game draw!")
