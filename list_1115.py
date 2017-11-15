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
'''
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
    print('goal')