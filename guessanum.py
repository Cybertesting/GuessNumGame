import random

guesstaken = 0
number = random.randint(1,20)

print('HelloWorld')
print('what is your name? ')
myName = input()
print ('well '+ myName + ' please guess a number')

for guesstaken in range(6):
    guess= input()
    guess = int(guess)

    if guess < number:
        print('you guess is too low')
    if guess > number:
        print('Your guess was too high')
    if guess == number:
       break

if guess == number:
    guesstaken = str(guesstaken + 1)
    print('Great guess you are right!  Only took you ' + guesstaken )

if guess!= number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number +'.')