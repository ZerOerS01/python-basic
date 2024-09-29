"""
    函数多返回值：
        语法：return 1,2....  
            —— 按照返回值的顺序，写对应顺序的多个变量接受即
            —— 变量之间用逗号隔开
            —— 支持不同类型的return
"""


# 演示
def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(f"x,y,z的值分别是：{x},{y},{z}")

"""
    根据使用方式上的不同，函数中有4种常见参数使用方式：
        1、位置参数：调用函数时根据函数定义的参数位置来传递参数
            注意：传递的参数和定义的参数的顺序及个数必须一致。
            
        2、关键字参数：函数调用时通过” 建=值 “形式传递参数
            作用：可以让函数更加清晰、容易使用，同时也消除了参数的顺序需求。
            注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序）
            
        3、缺省参数：默认参数，用于定义函数，为参数提供默认值，调用函数时不可传入该默认参数的值
            作用：当调用函数时没有传递参数，就会使用默认是缺省参数对应的值。
            注意：所有位置参数必须出现在默认参数前，包括函数定义和调用。函数调用时，如果为缺省参数传值则修改默认参数值，否则使用这个默认值
            *****默认值必须在最后，如果n-1个参数设置了默认值，n参数没有设置则会报错
            
        4、不定长参数：可变参数，用于不确定调用的时候会传递多少个参数(不传参也可以)的场景：
            作用：当调用函数时不确定参数个数时，可以使用不定长参数
            类型：1、位置传递：注意：传进的所有参数都会被args变量收集，他会根据进参数合并成一个元组(tuple)，args是元组类型，这就是位置传递
                 2、关键字传递：注意：参数是”键=值“形式的形式的情况下，所有的”键=值“都会被kwargs接受，并会根据”键=值“组成字典。
            
"""


# 位置参数：
def user_info(name, age, gender):
    print(f"您的名字是：{name}，年龄是：{age}，性别是：{gender}")


user_info('TOM', 20, '男')

# 关键字传参
user_info(name="小明", age=20, gender="男")
# 可以不按照固定顺序
user_info(age=20, gender="男", name="Tom")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
user_info("Tom", age=20, gender="男")


# 缺省参数：
def user_info2(name, age, gender='男'):
    print(f"姓名是:{name},年龄是：{age}，性别是：{gender}")


user_info2("小天", 16)
user_info2("小美", 17, '女')


# 位置传递不定长参数:语法：函数(*变量名)
def user_info3(*args):
    print(args)


# ('Tom',)
user_info3('Tom')
user_info3('Tom', 18, 'gg')


# 关键字传递不定长参数：语法：函数名(**变量名)
def user_info4(**kwargs):
    print(kwargs)


# {'name':'Tom','age':18,‘id’：110}
user_info4(name='Tom', age=18, id=110)

"""
        了解：函数都是接受数据作为参数传入：数字、字符串、字典、列表、元组等，但是数据本身，也可以作为参数传入另一个函数
                    将函数传入的作用：传入计算逻辑，而非传入数据。
        lambda匿名函数：
            定义：def关键字，可以定义带有名称的函数
                 lambda关键字，可以定义匿名函数(无名称)
            注意：由名称的函数，可以基于名称重复使用，而无名称的匿名函数，只可临时使用一次。
            语法：lambda 传入参数: 函数体(一行代码)
                    lambda是关键字，表示定义匿名函数；
                    传入参数表示匿名函数的形式参数，如：x，y表示接受2个形式参数；
                    函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码。
            
            
"""


# 函数作为参数传入函数中演示
# 函数compute，作为参数，传入了test_func函数中使用。
#   1、test_func需要一个函数作为参数传入，这个函数需要接受2个数字进行计算，计算逻辑由这个被传入函数决定.
#   2、compute函数接受2个数字对其进行计算，computer函数作为参数，传递给了test_func函数使用
#   3、最终，在test_func函数内部，由传入的compute函数，完成对数字的计算操作
def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)


def compute(x, y):
    return x + y

test_func(compute)


# lambda函数演示
def test_func(compute): # 通过def关键字，定义函数并传入
    result = compute(1, 2) # 传入实参给compute
    print(result) # 返回结果

test_func(lambda x,y: x + y) # 使用匿名函数定义参数，并把计算结果传入给compute
