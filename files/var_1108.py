#_*_ coding: utf-8 _*
# calculate 1+2+3+4 ....+100  的结果
flag = True
a = 0
res = 0

while a < 100:
    a += 1
    res += a
    falg = False
    # print(res)  是否缩进的结果不一致
print(res)

