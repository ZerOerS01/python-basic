"""
    数据容器字符串：不可修改
        定义：字符串中的每一个字符都是一个元素，每一个元素都有下标索引

"""
from operator import index

# 演示
my_str = "it hujiacheng and 205"
value = my_str[3]
value2 = my_str[-3]
print(value)   # 输出结果为 h
print(value2) # 输出结果为 2

# index方法查找
index1 = my_str.index("jiacheng")
print(index1) #输出结果为 5

# replace方法替换：
#     语法：字符串.replace(字符串1，字符串2)
#     功能：将字符串内的全部：字符串1，替换为字符串2，得到一个新的字符串
new_my_str = my_str.replace("it","程序")
print(new_my_str) #输出结果为"程序 hujiacheng and 205"

# split方法分割字符串：
#     语法：字符串.split(分隔符字符串)
#     功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中，得到一个新的列表对象(字符串本身不变)
my_str = "hello python ithujiacheng 205"
my_str_list = my_str.split(" ") # 通过空格来分割每一个字符串
print(my_str_list)  # 输出结果为["hello","python","ithujiacheng","205”]

# 字符串的规整操作（去前后空格）：语法字符串.strip()——默认不传入参数，去除首尾空格
my_str = "   ithjc and 205"
print(my_str.strip())     #输出结果为"ithjc and 205"
# 去前后字符串：语法：字符串.strip(字符串)
my_str = "21ithjc and 20512"
print(my_str.strip("21")) #传入参数相邻的2和1，去除首位2和1相邻的字符串  ，输出结果为"ithjc and 205"

# 统计字符串中某字符串的出现次数：
my_str = " iii  ithjc and 205"
count2 = my_str.count("i") # 使用count方法统计某字符串出现次数
print(count2) # 输出结果为 4

# 统计字符串长度
my_str = " iii  ithjc and 205"
num = len(my_str) # 使用len方法统计字符串长度
print(num) # 输出结果为19

# 字符串遍历：while
my_str = "黑马胡嘉诚" # 定义容器内容
index = 0 # 设置字符串下标索引条件
while index < len(my_str): # 当循环条件小于字符串长度 判断为True,保持循环，大于或等于则为Flag，退出循环
    print(my_str[index]) # 取出符合条件的字符串
    index += 1 # 每循环一次+1 ，保证有限循环

# 字符串遍历：for
my_str = "黑马胡嘉诚" # 定义容器内容
for index in range(len(my_str)):
    print(my_str[index])

# work
my_str = "ithjc itcast boxuegu" # 定义容器内容
# 统计字符串有多少"it"字符
num = my_str.count("it")
print(num)
# 将字符串内的空格，全部替换为字符"|"
new_my_str = my_str.replace(" ","|")
print(new_my_str)
# 并按照"|"进行字符串分割，得到列表
my_str_list = new_my_str.split("|")
print(my_str_list)