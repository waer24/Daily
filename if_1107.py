from random import randint
num =randint(5,20)
print('guess a num')
right = False

while right == False:
    answer = int(input())
    if answer < num:
        print("too small!")
    if answer > num:
        print("too big!")
    if answer == num:
        print("yeah!")
        right = True

