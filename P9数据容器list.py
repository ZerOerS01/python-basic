"""
    数据容器：
        定义：一个容器可以容纳多个数据，每份数据称为一个元素，每一个元素可以是任意类型的数据。
        根据特点的不同可，如
            是否支出重复元素
            是否可以修改
            是否有序，等
        分为五类，分别是：
        列表（list）、元组（tuple）、字符串（str）、集合（set）、字典（dict）


"""
from operator import index

# list（列表）
# 列表的定义：
#   字面量：[元素1,元素2,元素3,元素4,....]
#   定义变量: 变量名称 = [元素1,元素2,元素3,元素4,....]
#   定义空列表: 变量名称 = [] 或 变量名称 = list()
#   列表中的每一个数据称为元素，以[]作为标识，列表内每一个元素之间用，用逗号隔开
#   列表的特点:可以容纳(2**63-1\9223372036853775807个)
#            可以容纳不同类型的元素
#             数据是有序存储的(有下标序号)
#             允许重复数据尊重
#             可以增删改查等
# name_list = ['itheima',666,'python']
# print(name_list)
# print(type(name_list))


# # 列表的下标索引：从0-n
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])


# # 反向索引：从后往前，从-1开始，依次递减（-1、-2、-3....）
# print(name_list[-1])
# print(name_list[-2])
# print(name_list[-3])


# # 嵌套索引
# name_lists = [[123,'qweq'],[123545,'56sd']]
# print(name_lists[1][0])


# 列表的方法：函数是一个封装的代码单元，可以提供特定功能。将函数定义为class（类）的成员，那么函数会称之为：方法
#     方法和函数功能一样，有传入参数，有返回值值，指数方法的使用格式不同：
#     函数的使用：num = add(1,2)
#     方法的使用：student = Student()
#               num = student.add(1,2)


#   查看元素下标方法:
#     功能：查找指定元素在列表的下标，如果找不到，报错ValueError
#     语法：列表.index(元素)（index就是列表对象（变量）内置的方法（函数））
# index = name_list.index("itheima")
# print(f"itheima在列表中的下标索引值是：{index}")
# 错误示范：
# index = name_list.index("Hello")
# print(f"itheima在列表中的下标索引值是：{index}")


#   删除元素:语法1：del 列表下标
#           语法2：列表.pop(下标)
# del name_list[0]
# pop = name_list.pop(0)
#   删除某元素在列表中的第一个匹配项:语法: 列表.remove(元素)
# mylist = [1,2,3,4,5,6,7,0,0,8,7,6,5,4,3,2,1]
# mylist.remove(0)
# print(mylist)
#
#
#   清空列表:语法：列表.clear()
# mylist.clear()
# print(f"清空后的列表：{mylist}")


#   修改元素方法：语法：列表[下标] = 值
# my_list = [4,67,1]
# my_list[1] = 5
# print(my_list)


#   统计列表中某元素个数：语法：列表.count(元素)
# count = mylist.count(1)
# print(count)


#   统计列表中全部的元素数量:语法:len(列表)
# len = len(mylist)
# print(len)


#   插入元素方法：语法：列表.insert(下标，元素)
# my_list.insert(2,"我不是数字")
# print(my_list)


#   追加元素：语法：列表.append(元素)，将指定元素，追加到列表的尾部
# my_list.append("我要到最前面去!!!")
# print(my_list)
#   追加2：语法：列表.extend(其他数据容器)，将其他数据容器的内容取出，依次追加到尾部
# my_list.extend([1,5,4])
# print(my_list)



# # work
# # 定义列表记录学生年龄
# my_Student = [21,25,21,23,22,20]
# print(my_Student)
# # 追加数字31至尾部
# my_Student.append(31)
# print(my_Student)
# # 追加新列表[29,33,30],到列表尾部
# my_Student.extend([29,33,30])
# print(my_Student)
# # 取出(查看)第一个元素
# print(my_Student[0])
# # 取出(查看)最后一个元素
# print(my_Student[-1])
# # 查找元素31,在列表中的下标位置
# index = my_Student.index(31)
# print(f"查找元素31,他在列表中的下标位置是:{index}")


# while循环(迭代)遍历列表:定义:将容器内的元素依次取出进行处理的行为

#   遍历列表元素:
#        使用循环遍历
#   取出遍历列表元素:
#        使用列表[下标]的方式取出
#   控制循环条件:
#        定义变量表示下标,从0开始; 循环条件为下标值 < 列表的元素数量


# def my_list_while():
#     """
#     用while循环遍历列表演示函数
#     :return:None
#     """
#     my_list = ["胡家村","何嘉兴","殷龙威","王泽亮"]
# #   循环控制变量通过下标索引来控制,默认为0
# #   每一次循环下标变量+1
# #   循环条件: 下标索引变量 < 列表的元素数量
#
# #   定义一个变量用来标记列表的下标
#     index = 0   # 初始为0
#     while index < len(my_list):
#         # 通过index变量取出对应下标元素
#         ele = my_list[index]
#         print(f"列表的元素:{ele}")
#         # 至关重要 将循环变量(index) 每次循环+1
#         index += 1
#
# # for
# def my_list_for():
#     """
#     用for循环遍历列表演示函数
#     :return:
#     """
#     #for 临时变量 in 数据容器:
#     my_list = [1,2,3,4,5,6,7,8,9]
#     for eleS in my_list:
#         print(f"列表的元素有:{eleS}")
#
#
# my_list_while()
# my_list_for()

# work
# 定义两个列表内容
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list2 = [1,3,5,7,9]
def my_list_num():
    """
    使用while遍历
    :return:None

    """
    index = 0
    while index < len(my_list):
        if my_list[index] % 2 == 0:
            my_list2.append(my_list[index])
        index += 1
    print(my_list2)
my_list_num()


def my_list_num2():
    """
    使用for遍历
    :return:
    """
    for i in my_list:
        if i % 2 == 0:
            my_list2.append(i)
    print(my_list2)
my_list_num2()



