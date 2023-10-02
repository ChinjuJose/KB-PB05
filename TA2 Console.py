import random
r = random.randint(1,100)
#print(r)

win = 0
for i in range(1,4):
        
        number = int(input("Make a guess:"))
        
        if number != r:
            if number<r:
                print("Guess a bigger number")
            else:
                print("Guess a smaller number")
        else:
            print("You guessed it right! Congrats!")
            win = 1     
            break

if win==0:
    print("Oops! You Lost. Try again!")


