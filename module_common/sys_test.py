"""
    @author: xuanke
    @time: 2020/1/11
    @function: 对sys模块进行操作
"""
import sys


def test_dynamic():
    """
    sys动态属性
    :return:
    """
    # 接收命令行参数，更复杂的传参，可以使用argparse
    print(sys.argv)
    # 打印python解释器搜索模块的路径
    print(sys.path)
    # 获取已经加载的模块
    print(sys.modules)


def test_static():
    """
    sys静态属性
    :return:
    """
    # 获取python可执行文件的路径
    print(sys.executable)
    # 获取操作系统信息
    print(sys.platform)
    # 获取python内置的模块
    print(sys.builtin_module_names)
    # 获取python解释器版本信息
    print(sys.implementation)


def test_method():
    """
    sys方法
    :return:
    """
    # 打印python解释器默认编码
    print(sys.getdefaultencoding())
    # 打印对象的引用计数
    obj_1 = [1, 2]
    print(sys.getrefcount(obj_1))
    # 对象占用内存的大小
    print(sys.getsizeof(obj_1))
    # 退出程序
    # sys.exit(0)
    # 正常内容重定向
    sys.stdout.write("I am test\n")
    print("I am test2")
    # 错误内容重定向
    sys.stderr.write("I am error")
    # 读取内容,对比input
    print("please input something")
    content = sys.stdin.readline()
    print(content)

    stdout_1 = sys.stdout
    sys.stdout = open('text1.txt', 'w')
    print("ddd")
    print("qqq")
    sys.stdout = stdout_1
    print("111")


if __name__ == '__main__':
    test_method()
