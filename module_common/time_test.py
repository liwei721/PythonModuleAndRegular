"""
    @author: xuanke
    @time: 2020/1/2
    @function: 验证time模块
"""
import time
import datetime
import calendar


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

    # 将时间戳转为时间元祖,从1970年1月1日 0点0分计算
    print(time.gmtime(time_stamp))
    # 将时间戳转为时间元祖 ，本地时间，如果在中国就是从1970年1月1日 8点0分计算
    local_time_tuple = time.localtime(time_stamp)
    print(local_time_tuple)

    # 将时间元祖转成时间戳
    print(time.mktime(local_time_tuple))
    # 将时间元祖转成简单格式化
    print(time.asctime(local_time_tuple))
    # 将时间元祖格式化
    local_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time_tuple)
    print(local_time_str)

    # 将格式化的时间转成时间元祖
    print(time.strptime(local_time_str, "%Y-%m-%d %H:%M:%S"))

    print(time.perf_counter())
    # 时间戳简单格式化
    print(time.ctime(time_stamp))

    print(time.perf_counter())
    print(time.process_time())

def test_datetime():
    """
    对test_datetime 模块的方法进行验证
    :return:
    """
    # 生成时间,和日期没有关系，
    # 不过需要传入对应的Hour、Minutes、seconds、microsecond
    # 可用于时间的比较
    test_t = datetime.time(1, 2, 3, 4)
    print(test_t.minute)
    print(test_t.hour)
    print(test_t.second)

    print("*" * 20)
    # 生成简单型日期
    test_dt = datetime.date.today()
    print(test_dt.weekday())
    print(test_dt.month)
    print(test_dt.year)
    print(test_dt.day)
    # 从时间戳生成日期
    print(datetime.date.fromtimestamp(time.time()))
    # 从现有时间创建
    test_dt_1 = datetime.date(2019, 1, 6)
    print(test_dt_1.ctime())

    # 获取当前的日期和时间
    print("*" * 20)
    test_dt = datetime.datetime.today()
    print(test_dt)
    print(test_dt.time())
    print(test_dt.date())
    print(test_dt.now())
    print(test_dt.ctime())
    print(test_dt.weekday())
    print(test_dt.year)
    print(test_dt.day)
    # 从时间戳加载时间
    test_dt_stamp = datetime.datetime.fromtimestamp(time.time() - 10000)
    print(test_dt_stamp.now())
    print(test_dt_stamp.year)
    print(test_dt_stamp.month)
    # 从格列高利历序号加载时间，其中公元 1 年 1 月 1 日的序号为 1
    leap_num = calendar.leapdays(1,2020)
    test_dt_dinal = datetime.datetime.fromordinal(736942 + leap_num)
    print(test_dt_dinal)

    # 时间的计算
    print("*" * 20)
    test_today = datetime.datetime.today()
    print("today:", test_today)
    one_day = datetime.timedelta(days=1, hours=1, minutes=30)
    yesterday = test_today - one_day
    tomorrow = test_today + one_day
    print("yesterday:", yesterday)
    print("tomorrow:", tomorrow)
    # 也支持浮点数
    one_point_five_day = one_day * 1.5
    print(one_point_five_day)

    # 时间的比较
    print("*" * 20)
    d1 = datetime.datetime.today()
    d2 = d1 + datetime.timedelta(days=1)
    if d1 < d2:
        print("lasted date:", d2)

    # 时间的格式化
    today = datetime.datetime.today()
    today_format = today.strftime("%Y-%m-%d %H:%M:%S")
    print(today_format)

    # 将格式化的时间转成datetime
    today_d = datetime.datetime.strptime(today_format, "%Y-%m-%d %H:%M:%S")
    print(today_d)


def test_calendar():
    """
     对calendar进行验证
    :return:
    """
    # 打印一年的日历
    calen = calendar.calendar(2020)
    print(calen)

    # 打印一年某个月的日历
    calen_month = calendar.month(2020, 1)
    print(calen_month)

    # 根据指定的年月日计算星期几
    print(calendar.weekday(2020, 1, 7))

    # 根据指定日期获取时间信息，返回两个值，第一个值表示1号是星期几，第二个值是这个月有多少天
    print(calendar.monthrange(2019, 1))

    # 检测某一年是否是闰年
    print(calendar.isleap(2019))

    # 检测指定年限内闰年的数量
    print(calendar.leapdays(2008, 2020))


if __name__ == '__main__':
    # test_time()
    # test_datetime()
    test_calendar()
