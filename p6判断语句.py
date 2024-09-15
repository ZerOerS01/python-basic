# #
# print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
#
# age = int(input("请输入你的年龄:"))
# if age >= 18:
#    print("您已成年，游玩需要补票20元。")
#
# print("祝您游玩愉快。")
#
# #猜数字
# num = 4
#
# if int(input("请输入第一次猜想的数字：")) == num:
#     print("恭喜你，猜对了")
# elif int(input("不对，再猜一次：")) == num:
#     print("恭喜你，猜对了")
# elif int(input()) == num:
#     print("恭喜你，猜对了")
# else:
#     print("抱歉，猜错了")
#
#
# # if else if else 嵌套使用
# if int(input("你的身高为：")) >120:
#     print("抱歉，您的身高超出限制，需要补票15元。")
#     print("但是，如果您的VIP级别大于3，即可免费。")
#
#     if int(input("您的VIP等级为：")) >=3:
#         print("恭喜您，您可免费游玩。")
#     else:
#         print("抱歉，您的VIP级别小于3，需要补票15元。")
# else:
#     print("欢迎您的光临！！！")


# 嵌套猜数字
import random
num = random.randint(1,10)
guess_num = int(input("请输入猜想的数字："))
if guess_num != num:
    i