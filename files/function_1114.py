from random import randint

def isNum(num1,num2):
    if num1 < num2:
        print('too small')
        return False
    if num1 > num2:
        print('too big')
        return False
    if num1 == num2:
        print('equal')
        return True


num = randint(0, 100)
print('Guess what i thing?')
bingo = False

while bingo == False:
    answer = int(input())
    bingo = isNum(answer,num)

