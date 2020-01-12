"""
    @author: xuanke
    @time: 2020/1/11
    @function: 对logging多个模块使用的验证
"""
from module_common.logging_wrapper import Logger

logger = Logger()


def method_a():
    print(__name__)
    print("I am test_a")
    logger.error("logging test 2")
    logger.error("password is xxxxx")
    logger.info("pwd is xxxxx")

