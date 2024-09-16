"""

    集合:
    由于列表,元组,字符串存在局限性(都支持重复元素,如果场景需要对内容做去重处理,
    这些就不方便使用),而集合,最主要的特点就是:不支持元素重复(自带去重功能)、并且内容无序
    基本语法：
        定义集合字面量：{元素，元素，元素......}
        定义集合遍历：变量名称 = {元素，元素，元素......}
        定义空集合：变量名称 = set()
    *****集合不支持：下标索引访问，允许修改
"""
# 演示
my_set = {"sb","lao 6","asdasd","sb","lao 6","asdasd"}
my_set_empty = set()

# add方法，添加指定元素到集合内
my_set.add("hjchaoshuai")
print(my_set)

# remove方法：移除指定元素
my_set.remove("sb")
print(my_set)

# pop方法：从集合中随机取出元素
ele = my_set.pop()
print(ele)

# clear方法：清空集合
my_set.clear()
print(my_set)

# difference方法：取两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)    # 得到set1里面有，set2里面没有的元素集合{2,3}
print(set3)     # 得到新集合{2，3}，原集合不变

# difference_update方法：对比集合，删除调用方法的集合与被调用集合内相同的元素
set4 = {1,2,3}
set5 = {1,5,6}
set4.difference_update(set5)  # 删除ste4中和ste5内相同的元素1，得到集合{2,3},ste4被修改，ste5不变
print(set4)  # {2,3}

# unior方法：合并两个集合，得到新集合，原集合不变
set6 = set4.union(set5)
print(set6)

# count方法：统计集合元素数量
num = len(set6)
print(num)

#  不支持下标索引，不能用while循环，但是可以用for
for i in set6:
    print(i)


# work
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
num = set()
for i in my_list:
    num.add(i)

print(num)
