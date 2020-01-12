"""
    @author: xuanke
    @time: 2020/1/11
    @function: 验证shutil方法
"""
import shutil
import os
import logging


def copy_file_test():
    """
    验证文件copy
    :return:
    """
    # 对文件内容进行copy，使用路径
    copy_result = shutil.copyfile("text1.txt", "text2.txt")
    print(copy_result)

    # 对文件进行copy，使用Writer对象
    shutil.copyfileobj(open("test_file_1", "r"), open("text3.txt", "w"))

    # 对文件的stat进行copy
    print(os.stat("test_file_1"))
    print(os.stat("test_file"))
    shutil.copystat("test_file_1", "test_file")
    print(os.stat("test_file_1"))
    print(os.stat("test_file"))

    # 将文件text1.txt拷贝到test目录下面。
    copy_result_1 = shutil.copy("text1.txt", "test5.txt")
    print(copy_result_1)
    print(os.stat("text1.txt"))
    print(os.stat("test/text1.txt"))


def copy_folder_test():
    """
    对目录copy
    :return:
    """
    shutil.copytree("test", "test4", ignore=shutil.ignore_patterns("*.py", "*.png"))


def remove_folder_test():
    """
    递归删除目录
    :return:
    """
    # os.removedirs("test2")
    shutil.rmtree("test2")


def mv_test():
    """
    递归的移动文件
    :return:
    """
    shutil.move("test2", "test3")
    # shutil.move("test2/text2.txt", "text5.txt")


def archive_test():
    """
    对目录进行归档压缩
    :return:
    """
    format_result = shutil.get_archive_formats()
    print(format_result)
    # 将test3目录归档为zip
    shutil.make_archive("test3", "zip", "test2")

    # 将test3.zip进行解压
    shutil.unpack_archive("test3.zip", "test2")


def other_test():
    """
    其他方法验证
    :return:
    """
    # 获取磁盘利用情况
    disk_usage_result = shutil.disk_usage("test2")
    print(disk_usage_result)


if __name__ == '__main__':
    other_test()

