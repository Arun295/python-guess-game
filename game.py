import random
print('hello user')
print('welcome to guess game')
print('the computer will display your number of lives randomly')
words=('projects','groups','jobs','players','gamming','computers','farming','education','carrier')
required_word=random.choice(words)
print("guess the word")
life = [5, 6, 7, 8, 9, 10, 11, 12]
life = random.choice(life)
print("you have", life, 'lives')
guesses=''
fail = 0
while life > 0:
    for char in words:
     if char in guesses:
        print(char)
     else:
      print("_")
      fail+=1
    if fail ==0:
         print("you win")
         print("The word is: ", required_word)
         break
    guess = input("guess a character:")
    guesses += guess
    if guess not in required_word:
        life -= 1
        print("Wrong")
        print("You have", life, 'more guesses')
        if life == 0:
            print("You Loose")
            print('word is', required_word)