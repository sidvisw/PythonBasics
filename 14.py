n=18
guess=9
while(1):
    if(guess==0):
        print("game over")
        break
    guess_num=int(input("enter ur guess="))
    if guess_num>n:
        print("your guess is greater than the actual no.")
        guess=guess-1
        print("guess remaining=",guess)
    elif guess_num<n:
        print("your guess is less than the actual no.")
        guess=guess-1
        print("guess remaining=",guess)
    else:
        print("congrats ur guess is correct")
        print("u took",10-guess,"guesses to win")
        break
