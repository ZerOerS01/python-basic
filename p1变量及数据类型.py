"""

变量：在程序运行时，能存储计算结果或能表示值的抽象概念。
简单的说，变量就是在程序运行是，记录数据用的。

变量的定义格式
变量名称 = 变量的值
"""
from colorsys import rgb_to_yiq

# 演示
# 定义一个变量，用来记录钱包余额
money = 50
# 通过print语句输出变量内容
print("钱包余额：",money)

# 买了一个冰淇淋，花费10元

money = money-10

print("钱包余额：",money)



# type语句——用于验证数据类型，例如：type(被查看类型的数据)
print(type(money))
print(type("傻逼！！！"))

# 用变量存储type()的结果(返回值)：
Str_type = type("傻逼！！！")
Int_type = type(money)

print(Int_type)
print(Str_type)
# 变量无类型 但变量存储的数据有类型

"""
数据类型转换语句：
    int(x)——转换为整型
    float(x)——转换为浮点型
    str(x)——转换为字符串型
该语句都是带有结果的返回值

"""