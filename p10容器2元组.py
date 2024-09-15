"""
    数据容器（元组）：不能被修改
        定义：和list一样，使用小括号定义，逗号隔开
"""
# 定义元组：(元素，元素，元素，....)
# 定义元组变量：变量名称 = (元素，元素，元素,.....)
# 定义空元组：变量名称 = ()  或者  变量名称 = tuple()
# 定义单个元素的元组，元素后必须+,
# t1 = (12, )
# 元组嵌套
# t2 = ((1,2,3),(1,2))
# print(t2[0][1])
# num = t2[0][2]

# 元组的方法：
t3 = (1,3,3,3,3,3,2,3,4,5,6,7,8,90)
#   index()：查找某个数据，返回对应的下标，否则报错
index = t3.index(4)
print(index)
#   count(): 统计某个数据在当前元组出现的次数
count = t3.count(3)
print(count)
#   len(元组): 统计元组内的元素个数
len1 = len(t3)
print(len1)

# 元组的遍历：while
index = 0
while index < len(t3):
    print(t3[index])
    index += 1

# 元组的遍历：for
for index in range(len(t3)):
    print(t3[index])

# 嵌套
t4 = (1,2,["itheima","it205"])
print(t4)
t4[2][1] = "it胡嘉诚"
print(t4)

# work
# 定义学生数据容器
yz = ('周杰伦',11,['football','music'])
# 查询学生年龄所在的下标
index1 = yz.index(11)
print(index1)
# 查询学生的姓名
print(yz[0])
# 删除学生爱好中的football
del yz[2][0]
print(yz)
# 增加爱好：coding到爱好list内
my_list = yz[2]
my_list.insert(0,'coding')
print(yz)