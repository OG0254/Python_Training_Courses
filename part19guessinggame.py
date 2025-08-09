import random # it's preinstalled in python

score = 10
randomNumber = random.randint(1,10)

while True:
    userNumberInput = int(input('Guess : '))

    if userNumberInput == randomNumber:
        print("Congratulations you guessed it right! your score is " + str(score))
        break
    else:
        print('better luck next time')
        score -= 1 # if user guesses incorectly they reduce their score by 1
    if score == 0:  # Check if score reaches 0
        print("Game Over! The correct number was", randomNumber) # Point to note Python randomly picks a number between 1 and 10 each time the program runs. So, there isn't a specific "correct" number that you always need to input—it's different every time! 🎲

