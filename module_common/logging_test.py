"""
    @author: xuanke
    @time: 2020/1/11
    @function: 对logging模块进行验证
"""
import logging

from module_common import logging_test_2


def scene_one_test():
    """
    将不同级别的日志写到不同的地方
    :return:
    """
    # 获取记录器，默认的日志级别是warning的
    local_logger = logging.getLogger(__name__)
    local_logger.setLevel(logging.DEBUG)

    # 定义formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # 创建文件的fileHandler
    file_handler = logging.FileHandler("file.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    # 创建控制台的handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    local_logger.addHandler(console_handler)
    local_logger.addHandler(file_handler)

    local_logger.info("console a")
    local_logger.warning("console b")
    local_logger.error("console c")
    local_logger.critical("console d")


def scene_two_test():
    """
    封装一个简单的logutil，在这里调用
    :return:
    """
    logging_test_2.method_a()


def scene_three_test():
    """
    使用filter过滤password的日志
    :return:
    """
    logging_test_2.method_a()


if __name__ == '__main__':
    scene_three_test()
