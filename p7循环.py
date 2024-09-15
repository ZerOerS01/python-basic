# # while循环
# i = 0
# while i < 50 :
#     print("玩辣QAQ")
#     i += 1
"""

# 猜数字
import random
num = random.randint(1,50)
flag = True
j = 0

while flag:
   guess_num = int(input("请输入您的猜想数字:"))
   j += 1
   if guess_num == num:
       print("恭喜您猜对了!!!")
       flag = False
   else:
       if guess_num > num:
           print("很遗憾，您猜测的数字大了。")
       else:
           print("很遗憾，您猜测的数字小了")

print(f"本次猜数字次数为：{j}")

"""
from p1变量及数据类型 import money

"""

# while嵌套
i = 1
while i <= 100:
    print(f"今天是第{i},准备表白。。。")

    j = 1
    while j <= 10:
        print(f"送给小美第{j}朵玫瑰花")
        j += 1

    print("我们的爱情就像一个急刹")
    i += 1

print(f"已坚持{i-1}，表白成功")


# 九九乘法表
i = 1

while i <= 9:

    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t",end="")
        j += 1
    i += 1
    print()

"""

# for循环（遍历循环）

# name = "hujiacheng"
#
# for x in name:
#     #将name的内容，挨个去除赋予x临时变量
#     #就可以在循环体内进行处理
#     print(x)
#
#name = "ithujiachenaag"
# i = 0
# for x in name:
#     print(x)
#     if x == 'a':
#         i += 1
#
# print(f"共含有:{i}个字母a")

"""

# rang语句，
# 语法1：range(num)——从0开始到num
for x in range(10):
    print(x)
# 语法2：range(num1,num2)——从num1开始遍历到num2
for i in range(3,6):
    print(i)
# 语法3：range(num1,num2,step)——从num1开始按照步长遍历到num2，以step为准（step默认为1）
for j in range(3,12,2):
    print(j)
    
"""

# num = 50
# j=0
# for i in range(1,50):
#     print(i)
#     if i % 2 == 0:
#         j += 1
#
# print(f"有{j}个偶数")

# # for循环嵌套
# i = 0
# for i in range(1,101):
#     print(f"今天是第{i}天")
#     for j in range(1,11):
#         print(f"送给小美的第{j}朵玫瑰")
#
#     print("小美我喜欢你")
#
# print(f"以坚持{i}天，表白成功")
#
# # 九九乘法表
# # 通过外层循环控制行数
# for i in range(1,10):
#     j=1
#     # 通过内层循环中输出每一行的内容
#     while j<=i:
#         print(f"{i} * {j} = {j * i}\t",end="")
#         j += 1
#     # 外层循环可以通过print输出一个回车符
#     print()
#
# i = 1
# while i <= 9:
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {j * i}\t",end="")
#     i += 1
#
#     print()

"""

# 演示循环中断语句 continue
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")

# 嵌套continue
for i in range(1,6):
    print("语句1")
    for j in range(1,i+1):
        print("语句2")
        continue
        print("语句3")

    print("语句4")


# 演示循环中断语句 break
for i in range(1,10):
    print("语句1")
    break
    print("语句2")

print("语句3")

# 嵌套break

for i in range(1,6):
    print("yuju1")
    for j in range(1,i+1):
        print("yuju2")
        break
        print("yuju3")

    print("yuju4")

"""


money = 10000
wage = 1000
for i in range(1,21):
    import random
    point = random.randint(1,10)
    if point < 5 :
        print(f"员工{i}，绩效分{point},低于5，不发工资")
    else:
        print(f"员工{i}发放工资{wage}，账户余额还剩余{money - wage}")
        money = money - wage
        if money == 0:
            break

print("工资已全部发完，没拿到工资的同志请下次再来")