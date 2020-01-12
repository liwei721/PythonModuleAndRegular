"""
    @author: xuanke
    @time: 2020/1/7
    @function: 对os模块的练习
"""
import os


def folder_operation_test():
    """
    对目录进行增、删、改操作
    :return:
    """
    # 创建一个目录,如果已经存在目录，则抛出OSError:[Errno 66] Directory not empty
    if not os.path.exists("test_folder"):
        os.mkdir("test_folder")

    # 递归创建目录,exist_ok=false,表示目录存在抛出异常
    os.makedirs("test_folder/a/b/c", exist_ok=False)

    # 重命名文件
    os.rename("test_folder", "test")
    # 重命名多级目录
    os.renames("test/a", "test/aa/a")

    # 遍历目录test
    result = os.listdir("test")
    print(result)

    print("*" * 20)
    list_result = os.walk("test")
    for parent, dir_name, file_name in list_result:
        print(parent)
        print(dir_name)
        print(file_name)

    print("*" * 20)
    with os.scandir("test") as scan_dir:
        for entity in scan_dir:
            print(entity.name)

    # # 删除一个目录
    # os.rmdir("test/aa/a/b/c")
    # # 递归删除目录
    # os.removedirs("test/aa/a/b")


def folder_test():
    """
    对目录查询和文件属性查询
    :return:
    """

    # os.mkdir("test")
    # 判断路径是否存在
    print(os.path.exists("test"))
    # 判断路径是否为folder
    print(os.path.isdir("test"))
    # 判断路径是否是文件
    print(os.path.isfile("test"))

    # 获取文件的属性
    print(os.path.getctime("test"))
    print(os.path.getmtime("test"))
    print(os.path.getsize("test"))
    print(os.stat("test"))

    # 创建文件，并写入内容
    fd = os.open("test_file", os.O_RDWR | os.O_CREAT)
    os.write(fd, b"this is a test")
    os.close(fd)

    # 直接使用open方法
    with open("test_file_1", "wb") as f:
        # 这里返回的是一个操作文件的BufferedWriter对象
        print(f)
        f.write(b"this is a test")

    # os.rmdir("test")


def path_operation_test():
    """
    对路径进行操作的验证
    :return:
    """
    # 获取当前的工作目录，绝对路径
    print(os.getcwd())

    # 上级目录
    print(os.pardir)

    # 用于改变当前工作目录
    os.chdir("..")
    print(os.getcwd())

    # 返回路径所在目录
    print(os.path.dirname("."))
    print(os.path.abspath(os.path.dirname(".")))

    # 获取绝对路径
    print(os.path.abspath("."))
    # 判断路径是否是绝对路径
    print(os.path.isabs("."))
    # 路径拼接
    print(os.path.join(".", "a", "b"))

    # 路径拆分,比如：传入a/b/c/d  返回： a/b/c , d
    print(os.path.split(os.getcwd()))

    # 将传入的path，分割为路径和文件扩展名
    print(os.path.splitext(os.getcwd()))


def system_cmd_test():
    """
     执行系统命令的测试
    :return:
    """
    os.system("dir")
    os.system("python -V")

    # python有更强大的subprocess，之后会介绍
    with os.popen("dir", "r", 1) as f:
        print(type(f))
        print(f.read())


def system_operation_test():
    """
    获取系统信息的方法
    :return:
    """
    # 返回当前进程的id
    print(os.getpid())
    # 返回操作系统的信息,注意在windows上运行会报错。不支持windows
    print(os.uname())
    # 返回系统的环境变量
    print(os.environ)
    # 返回系统的环境变量，PATH对应的值
    print(os.environ.get('PATH'))


if __name__ == '__main__':
    path_operation_test()
