import keyword
str1 = 'good'
str2 = 'bad'
print (str1 + str2)

num =25
name = 'darcy'
print("my ages is " + str(num))
# my age is 18 ,有+

print('my age is %d' % num)
# my age is 18，以下都没有+

print('my age is %f'% num)
# my age is 18.000000

print('my age is %.2f' %num)
# my age is 18.00

print('my age is %s' % '18')
# my age is 18

print('my age is %s' % num)
# my age is 18

print('%s my age is' % num)
# 18 my age is

print('%s, wait a moment' % name)
print('Do you know, %d' % num)

#多个for循环的嵌套
for i in range(0,5):
    for j in range(0,5):
        print(i,j)


#for循环打印星星
for i in range(0,5):
    for j in range(0,5):
        print(j * '*')
    print('')


#print tuple
print('%s ,she seems not too exciting, because she\'s examination only %d score' % ('darcy',50))

#类型转换
print(bool(-123))
print(bool(0))
print(bool('123'))
print(bool('abc'))
print(bool('False'))
# ‘False’是一个不为空的字符串，当被转换成bool类型之后，就得到True。
print(bool(''))
print(bool(' '))
# 一个空格也不能算作空字符串。

a = '123'
if a:
     print('right')

def sayHello():
    print('hello world')
sayHello()

def who(someone,something):
    print(someone +' always say:'+something + ' is wonderful' )
who('darcy','play piano')