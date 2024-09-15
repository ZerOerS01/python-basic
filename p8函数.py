"""
    函数：
        封装好的；
        可重复使用的；
        用来实现特定功能的代码段

    好处：
        将所需功能封装在函数内，可重复使用
        提高代码的复用性，减少重复代码，提高开发效率
    函数的基础定义语法:
        def 函数名(传入参数):
            函数体
            return 返回值
    调用函数：
        函数名(参数)
*****参数与返回值如不需要，可以省略
*****函数必须先定义后使用

"""
from imaplib import Flags

# # 定义一个函数，用来计算字符串长度
# str1 = "asdasdqwef"
# def my_lef(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"字符串{data}的长度是{count}")
#
# my_lef(str1)

# def my_hs():
#     print("欢迎来到205！")
#     print("请说出我们的口号")
# my_hs()

"""
    函数的传入参数：在函数进行计算的时候，接受外部（调用时）提供的数据
    参数之间用逗号分隔，参数分为形参和实参：
        举例子，my_num(5,7)中的5,7就是实参，真正需要用到的参数
        而my_num(x,y)中的x,y就是形参，表示将要使用两个参数
        
    传入参数的数量是不受限制的，可以多个参数，也可以不给。
"""

# # 传参示例
# def my_num(x,y):
#     num=x+y
#     print(f"{x} + {y} 的结果是 {num}")
#
# my_num(5,7)

"""
    函数的返回值：
        定义：程序中函数完成事情后，最后给调用者的结果
        作用：返回函数的计算结果。
        函数体在遇到return后就结束了，所以在return后的代码不执行
        
    None类型：
        字面量None，类型为<class 'NoneType'>
        没有使用return的函数也有返回值，返回值为None
        作用
            1、用在函数无返回值上
            2、用在if判断上：在if语句中，None等同于False，一般用于在函数中主动返回None，配合if判断
            3、用于声明无内容的变量上：name = None
"""
# 简单定义一个两数相加功能
# 函数说明文档：对函数进行解释说明，帮助更好理解函数
# def add(a,b):
#     """
#     add函数可以接受2个参数，进行2数相加的功能
#     :param a: 形参a表示相加的其中一个数字
#     :param b: 形参b表示相加的另一个数字
#     :return:  返回值是2数相加的结果
#     """
#     num = a+b
#     return num
#
# r = add(6,2)
# print(r)
# print(add(123,677))

# 函数的嵌套调用：在函数中调用另一个函数，例如：
# def func_b():
#     print("aaaaaa")
#
# def func_c():
#     print("bbbbbb")
#     func_b()
#     print("cccccc")
# func_c()

"""
    变量在函数中的作用域（变量在哪里可用，哪里不可用）：
        局部变量（在函数内定义）：定义在函数体内部的变量，旨在函数体内生效，在外部调用将报错
        全局变量（在函数外定义）：在函数体内、外都能生效的变量
    
    global关键字：可以在函数内部声明变量为全局变量
"""
# num = 100
# def tes():
#     print(num)
# def tesb():
#     num=200
#     print(num)
# def tesc():
#     # global 关键字声明num为全局变量
#     global num
#     num = 900
#     print(num)
#
# tes()
# tesb()
# tesc()


# # wrok——黑马ATM

money = 5000000
name = input("请输入您的姓名：")

def look(show_1):
    if show_1:
        print("----------查询余额----------")
    print(f"{name},您好，当前您的余额为：{money}")

def dep(num):
    global money
    money = money + num
    print("----------存款----------")
    print(f"{name},您好，您以成功存款{money}元")
    look(False)
def wit(num2):
    global money
    money = money - num2
    print("----------取款----------")
    print(f"{name},您好，您以成功取款{money}元")
    look(False)

def main():
    print(f"----------主菜单----------\n{name},您好，欢迎来到205银行ATm。请选择操作：\n查询余额\t\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]\n") # 用转移字符\t来对齐
    return input("请输入您的选择：")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        look(True)
        continue
    elif keyboard_input == "2":
        dep(int(input("请输入您要存款的金额：")))
        continue
    elif keyboard_input == "3":
        wit(int(input("请输入您要取款的金额：")))
        continue
    else:
        print("正在退出程序!请稍等")
        break

