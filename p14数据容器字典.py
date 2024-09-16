"""

    字典（不允许重复元素）：
        定义：像字典一样，并且和集合一样使用{}定义，不过存储的元素是一个个的：键值对
        作用：通过key找到value
        语法：
            定义字典字面量：{key:value,key:value,key:value,.....}
            定义字典变量：变量名称 = {key:value,key:value,key:value,.....}
            定义空字典：1、变量名称 = {}
                      2、变量名称 = dict()

            字典的Key和Value可以是任意数据类型(Key不可为字典)，因此表面，字典可以嵌套

"""
# 演示
my_dict = {"王里红":99,"邹杰论":88,"林俊节":77}  # 定义字典

# 字典数据的获取：语法，字典[key]可以取到对应的Value
score = my_dict["王里红"]
print(score)

# 定义嵌套字典
my_dict = {"王力红":{"语文":77,"数学":66,"英语":33},
           "周杰轮":{"语文":88,"数学":86,"英语":55},
           "林俊节":{"语文":99,"数学":96,"英语":66}
}
score = my_dict["王力红"]
print(score)
score = my_dict["林俊节"]["语文"]
print(score)

# 新增元素：语法：字典[Key]=Value，结果：字典被修改，新增了元素
my_dict = {
    "王力红":99,
    "周杰轮":88,
    "林俊节":77
}
my_dict["张学油"] = 66  # 新增元素，张学油的考试成绩
print(my_dict)

# 更新元素：语法：字典[Key]=Value，结果：字典被修改，元素被更新
my_dict["王力红"] = 90  # 更新元素,王力红成绩更改为90
print(my_dict)

# 删除元素:语法:字典.pop(Key),结果:获得指定Key的Value,字典被修改,指定Key被删除
value = my_dict.pop("张学油")
print(value) # 通过Key张学油获取到了其value值
print(my_dict)

# 清空元素:语法:cleal
# my_dict.clear()
# print(my_dict) # 清空字典

# 获取全部的Key:语法:字典.keys(),结果:得到字典中的全部Key
keys = my_dict.keys()
print(keys)

# 遍历字典:for
# 方式1:通过获取到全部的Key来完成遍历
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的Value是:{my_dict[key]}")

# 方式2:直接对字典进行for循环,每一次循环都是直接得到Key
for i in my_dict:
    print(f"字典2的key是:{i}")
    print(f"字典2的Value是:{my_dict[i]}")

# 统计字典内的元素数量
num = len(my_dict)
print(num)


# work
my_dict = {
    "王力红":{
        "部门":"科技部",'工资': 3000,'级别':1
    },
    "周杰轮":{
        "部门":"市场部",'工资': 5000,'级别':2
    },
    "林俊节":{
        "部门":"市场部",'工资': 7000,'级别':3
    },
    "张学油":{
        "部门":"科技部",'工资': 4000,'级别':1
    },
    "刘德滑":{
        "部门":"市场部",'工资': 6000,'级别':2
    },
}

for i in my_dict:
    if my_dict[i]["级别"] == 1:
        my_dict1 = my_dict[i]
        my_dict1["级别"] = 2
        my_dict1['工资'] += 1000

print(my_dict)