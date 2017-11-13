print('you are a \'Bad\' man')
print("this is the\nsame line")
print('He said ,"I\'m yours!"')
print('\\\_v_//')
print('Stay hungry,\nstay foolish.\n\t\t--Steve Jobs')

# 用python输入一串星星
print('Please enter a num, i can make it bocome a star form')
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

# 用python输入   等腰三角形
print('Please enter a num, i can make it bocome a Isosceles triangle')
n = int(input())
a = 1
print('*')
for n in range(1, n+1):
    if n < 5:
        a += 2
        str = print(a * '*')
