#输入一个大于等于3的值n，输出斐波纳契数列的前n项。
# 注：斐波纳契数列：1,1,2,3,5,8,13,21...前两项为1，从第3项起，每一项是前两项的和

# print('please enter  a number:')
# num = int(input())
# i = 0
# sum = 0
# res = []
#
# if i == 0:
#     for i in range(1,2):
#         i += 1
#         sum = 1
#         res = sum
#         print(res)
# if i >= 2:
#     for i in range(1,num):
#         res = (i-1) + (i-2)
#         i += 1
#         print(res)



#  我想的太复杂了,一定有两个变量，前后赋值
num = print('Please write a number and I can figure out the Fabonacci sequence fot that number')
n = int(input())
sum = 0
a1 = 1
a2 = 1
for n in range(1,n+1):
    if n <= 2:
        print(a1)
    if n >= 3:
        sum = a1 + a2
        print (sum)
        a1 = a2
        a2 = sum


