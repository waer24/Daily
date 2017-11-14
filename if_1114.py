'''from random import randint
def compassNum(num1,num2):
    if num1 < num2:
        print("too small")
        return False
    elif num1 > num2:
        print('too big')
        return False
    else:
        print('equal')
        return True

print('Please write a number and let me guess')

num = randint(0,100)
bingo = False
while bingo == False:
    answer = int(input())
    bingo = compassNum(answer,num)'''

def getQuadrant(x,y):
    if x >= 0:
        if y >= 0:
            print('1st quadrant')
            return False
        else:
            print('4th quadrant')
            return False
    if x <= 0:
        if y >= 0:
            print('2nd quadrant')
        else:
            print('3rd quadrant')
getQuadrant(23,-59)


