num = 10
print('Guess what i think?')
answer = int(input())


result = answer < num
print ('too small?')
print (result)

result = answer > num
print('too big?')
print(result)

result = answer == num
print('equal?')
print (result)

num = 40
print('please let me guess a number,ok ?')
answer2 = int(input())

result = answer2 < num
print('too big?')
print(result)




