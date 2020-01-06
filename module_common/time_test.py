"""
    @author: xuanke
    @time: 2020/1/2
    @function: 验证time模块
"""
import time
import datetime


def test_time():
    """
    对test_time模块的方法进行验证
    :return:
    """
    # 获取时间戳
    time_stamp = time.time()
    print(time_stamp)
    # 计算时间戳的含义。
    print(time_stamp / 3600 / 24 / 365 + 1970)

    print(time.localtime(time_stamp))
    print(time.asctime())
    print(time.gmtime(time_stamp))
    print(time.mktime(time.localtime()))


def test_datetime():
    """
    对test_datetime 模块的方法进行验证
    :return:
    """
    now_datetime = datetime.datetime.now()
    print(now_datetime)
    print(now_datetime.timestamp())
    print(now_datetime.day)
    print(now_datetime.minute)
    print(now_datetime.month)
    print(now_datetime.year)

    now_date = datetime.date.today()
    print(now_date)

    now_time = datetime.time
    print(now_time.minute)

    now_timezone = datetime.timezone
    print(now_timezone.max)


if __name__ == '__main__':
    test_time()
    print("*" * 20)
    test_datetime()
