"""
    @author: xuanke
    @time: 2020/1/11
    @function: 对logging方法封装
"""
import logging
import os
import sys

# 获取main方法所在的文件, a/b/c/d   a/b/c, d
main_file_name = os.path.split(os.path.splitext(sys.argv[0])[0])[1]


class Logger(object):
    __instance = None
    __init = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("new ")
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, logger_name=main_file_name):
        if not self.__init:
            print(logger_name)
            self.logger = logging.getLogger(logger_name)
            self.logger.setLevel(logging.DEBUG)
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

            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

            self.logger.addFilter(PasswordFilter())

            Logger.__init = True

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


class PasswordFilter(logging.Filter):
    def filter(self, record):
        if "password" in record.getMessage():
            return False
        if "pwd" in record.getMessage():
            return False
        return True
