"""

    异常：当检测到一个错误时，Python解释器就无法继续执行，反而出现了一些错误的提示，这就是异常(BUG)

    捕获异常：
        为什么要捕获异常：
            世界上没有完美的程序，任何程序在运行的过程中，都有可能出现异常，出现bug导致程序无法完美运行。
            我们要做的就是在力所能及的范围内，对可能出现的BUG，进行提前准备，提前处理
            当我们在程序中遇到了BUG，那么接下来有两种情况：
                1、整个程序因为一个BUG停止运行
                2、对BUG进行提醒，整个程序继续运行
            作用：提前假设某处会出现异常，做好提前准备，当真的出现异常时可以有后续手段
        捕获异常的语法格式：
            tyr:
                可能发生错误的代码
            except:
                如果出现异常执行的代码
"""
import time

# 基本异常捕获语法：
# try:
#     f = open("D:/XueXi/Python/xuexi/Work/YCyanshi.txt","r",encoding="utf-8")
# except:
#     print("出现异常了，因为文件不存在，将改为w模式去打开")
#     f = open("D:/XueXi/Python/xuexi/Work/YCyanshi.txt", "w", encoding="utf-8")
#     f.close()

# 捕获指定异常
# 注意：如果尝试执行的代码的异常类型和要捕获的异常类型和要捕获的异常类型不一致，则无法捕获异常，一般try下方只放一行尝试执行的代码
# try:
#     print(name)
# # except 异常类型名称 as 变量：      此方法可以打印异常
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)

# 捕获多个异常:捕获多个异常时，可以把要捕获的异常类型的名字
# try:
#     # print(1/0)
#     print(name)
# # 放到except后，使用元组的方式进行书写，用逗号隔开
# except(NameError,ZeroDivisionError):
#     print('ZeroDivision错误...')

# 捕获所有异常
# 第一种，基础捕获异常语法也可以称为捕获所有异常，因为没有给定异常类型
# 第二中, 给定一个顶级异常Exception的异常类型来匹配所有异常
# try:
#     # 1/0
#     print(name)
# except Exception as e:
#     print("出现异常了！！！")

"""
    
    异常else：表示如果没有异常要执行的代码。
    异常finally：表示无论是否异常都要执行的代码，例如关闭文件。
"""
# else示例
# try:
#     print(1)
# except Exception as e:
#     print(e)
# else:
#     print('我是else，没有异常的时候执行的代码')

# finally示例
# try:
#     f = open("D:/XueXi/Python/xuexi/Work/YCyanshi.txt", "r", encoding="utf-8")
# except Exception as e:
#     f = open("D:/XueXi/Python/xuexi/Work/YCyanshi.txt", "w", encoding="utf-8")
# else:
#     print('没有异常')
# finally:
#     f.close()

"""

    异常的传递性：异常具有传递性
        当函数func01中发生异常        
        
    Python模块：是一个Python文件，以.py结尾，模块能定义函数，类和变量，模块里能包含可执行的代码
        作用：Python中有很多各种不同的模块，可以快速实现一些功能，例如时功能time模块，我们可以认为
             我们可以认为一个模块就是一个工具包，每一个工具包中都有各种不同的工具供我们使用进而实现各种不同功能
        模块的导入方式：[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
            import 模块名:
            from 模块名 import 类、变量、方法等
            from 模块名 import *
            import 模块名 as 别名
            from 模块名 import 功能名 as 别名
            
"""
# time模块示例
# import time   # 导入Python内置的time的模块（time.py这个文件代码）
# print("开始")
# time.sleep(2) # 通过. 就可以使用模块内部的全部功能(类、函数、变量)
# print("结束")

# from 模块名 import 功能名
# from time import sleep
# print("开始")
# sleep(2)
# time.sleep(2)   # 不会报错，但会在顶上创建import time
# print("结束")

# * 导入time模块的全部功能
# from time import *  # *表示全部的意思
# print("开始")
# sleep(2)
# print("结束")

# as定义别名
# 模块定义别名 import 模块名 as 别名
# import time as tt
# print(1)
# tt.sleep(2)
# print(2)

# from 模块名 import 功能 as 别名
# from time import sleep as sl
# print(1)
# sl(2)
# print(2)

"""

    自定义模块：
        了解自定义模块并使用：
            注意：1、每个Python文件都可以作为一个模块，模块的名字就是文件名，也就是自定义模块名必须符合标识符命名规则。
                 2、当导入多个模块的时候，且模块内有同名功能，当调用这个同名功能的时候，调用的时后面导入的模块功能
            测试模块：在实际开发中，当开发人员编写万一个模块后，为了让模块能够在项目中达到想要的效果
                    开发人员会自行在py文件中添加一些测试信息，例如在文件中添加测试代码test（1，2）
                问题：此时，无论是当前文件，还是其他以及导入了该模块的文件，在运行的时候都会自行执行‘test’函数的调用
                解决方案:例如：
                    def test(a,b):
                        print(a + b)
                    
                    if_name_=='_main_':  # 只有在当前文件中调用该函数，其他导入的文件内不符合该文件条件，则不执行test函数调用
                        test(1,1)
        了解 mian 变量的作用：

"""
# 创建函数方法
# def test(a,b):
#     print(a + b)
# 在其他文件使用import 文件名；如何在文件中使用文件名.方法名
# 或者使用from 文件名 import 方法名

# 模块1代码
# def my_test(a,b):
#     print(a + b)

# 模块2代码
# def my_test(a,b):
#     print(a - b)

# 导入模块和调用功能代码
# from 文件名1 import my.test
# from 文件名2 import my.test

# my_test函数时模块2中的函数:a - b
# my_test(1,1)

# 测试模块