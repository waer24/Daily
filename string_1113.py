print('you are a \'Bad\' man')
print("this is the\nsame line")
print('He said ,"I\'m yours!"')
print('\\\_v_//')
print('Stay hungry,\nstay foolish.\n\t\t--Steve Jobs')

# 用python输入一串星星
print('please write a number and i can draw a 5-line star-filled triangle')
n = int(input())
a = 1
print('*')
for n in range(1, n+1):
    if n < 3:
        a += 2
        str = print(a * '*')
    if n > 3:
        a -= 2
        str = print(a * '*')
#用两个for循环的方法：
for i in range(0,5):
    for j in range(0,5):
        print(j * '*')
    print('')


#while 的写法
print("please write a number and i can draw a star-filled triangle")
n = int(input())
a = 1
x = 1

print(a * '*')
while x <= n:
    if x < n / 2:
        a += 2
        print(a * '*')
    else:
        a -= 2
        print(a * '*')
    x += 1



# 用python输入   等腰三角形
print('Please enter a num, i can make it bocome a Isosceles triangle')
n = int(input())
a = 1
print('*')
for n in range(1, n+1):
    if n < 5:
        a += 2
        str = print(a * '*')


#字符串的分割#
s = 'maybe i should do more and less talk'
print(s. split())

#字符串的拼接#
a = ['a','b','c']
s = ','
b = s.join(a)
print(b)

