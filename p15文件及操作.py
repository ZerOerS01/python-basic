"""
    文件编码：
        文本文件是使用编码技术(密码本)将内容翻译成0和1存入
        编码技术：翻译的规则，记录了如何将内容翻译成二进制，以及如何将二进制翻译回可识别内容
"""
"""

    文件的读取：
        1、open()打开方法：可以打开一个已存在的文件，或者创建一个新的文件；
            语法：open(name,mode,encoding)：f = open('python.txt','r','encoding="UTF-8  ")
                name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)
                mode:设置打开文件的模式(访问模式)：只读r、写入w、追加a等。
                encoding:编码格式(推荐使用UTF-8)
        2、read()读取方法：
            语法：文件对象.read(num),num表示要从文件中读取的数据长度(单位是字节)，如果没有传入参数，则读取全部数据
           readlines()方法：可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
           readline()方法：一次读取一行内容
           for line in 文件对象
        3、close()关闭文件方法：
            with open(”python.txt“,"r") as f:  ——通过在with open的语句块对文件进行操作，可以在操作完成后自动关闭close文件，避免遗忘掉close方法
    
    文件的写入：
        1、write(内容)方法：文件写入
        2、flush()方法内容刷新
            注意：直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
                 当调用flush的时候，内容会真正写入文件，这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写入硬盘）

"""
# 写入演示
# 打开文件，不存在的文件
# f = open("D:/XueXi/Python/xuexi/Work/test.txt","w",encoding="UTF-8") # 打开不存在的文件，会在该路径下创建一个新文件
# # weite写入
# f.write("Hello World！！！")
# # flush刷新，不刷新，内容会在缓冲区而不会写进硬盘文件中
# f.flush()
# # close关闭
# f.close()
# 打开一个存在的文件,w模式，文件不存在，会创建新闻界。w模式，文件存在，会清空原有内容
# f = open("D:/XueXi/Python/xuexi/Work/test.txt","w",encoding="UTF-8")
# # write写入，flush刷新
# f.write("IT胡嘉诚") # 此时的文件内容会覆盖之前的内容，因为使用的是打开文件W模式。w
# f.flush()
# # close关闭，colse自带flush()方法功能，写了close不需要手动写flush
# f.close()


# 追加演示
# 打开文件，通过a模式打开即可
f = open("D:/XueXi/Python/xuexi/Work/test.txt","a",encoding="UTF-8") # 注意: a模式，文件不存在会创建文件，文件存在会在最后追加写入文件
# 文件写入
f.write("\nWDF,丢勒楼某")
# 关闭并刷新
f.close()