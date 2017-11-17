'''
a = ['a',666,'bule',12,13,90]
a.append(45)
print(a)

del(a[0])
# not a.del(a[0])
print(a)

a[2] = 'orange'
print(a)

print(a[0])


from random import choice
print('please choice a direction to shoot')
print('left','center','right')
your = input()
print('your kicked:' + your)
direction = ['left','center','right']
bingo = choice(direction)

if your != bingo:
    print('oops')
    print('computer kicked ' + bingo)
else:
    print('goal！')
'''

#点球小游戏#
from random import choice
score_you = 0
score_com = 0
dir = ['left','center','right']
for i in range(0,5):
    print('please choice a direction to shoot:left? center ? right?')
    your = input()
    bingo = choice(dir)
    if bingo == your:
        print('yes! goal!!,you still have %d times' % (5-i))
        score_you += 1
    else:
        print('no,one more try')
        score_com += 1
    print('Your score is : %d' % score_you)
    print('The computer score is %d' % score_com)