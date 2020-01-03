"""
    @author: xuanke
    @time: 2020/1/1
    @function: 验证module random
"""
import random
import collections

counter = collections.Counter()  # 用Counter统计次数。


def test_int():
    """
     随机生成int类型的数字
    :return:
    """
    # 0-2之间的整数
    print(random.randrange(3))
    # 1-299之间的整数，增长基数是5
    print(random.randrange(1, 300, 5))
    # 1-20之间的整数
    print(random.randint(1, 20))
    # -3到0之间的负数
    print(random.randint(-3, 0))
    # -3到-1之间的负数
    print(random.randrange(-3, 0))

    # 返回1~2-1之间的数字
    print(random.randrange(1))
    # 返回1~2的32次方-1之间的数字
    print(random.getrandbits(32))


def test_float():
    """
    随机生成浮点数，其实也用了数学分布
    :return:
    """
    # 1. 生成一个0-1之间随机浮点数
    print(random.random())
    # 2. 生成一个a-b之间的随机浮点数
    print(random.uniform(10, 500))
    print(random.uniform(40, 10))


def test_seq():
    """
     对序列进行操作
    :return:
    """
    # 从给定的序列中随机选择一个元素
    print(random.choice([1, 2, 3, 4, 5]))
    # random.choice的升级版本，还可以指定某个元素对应的权重
    print(random.choices([1, 2, 3, 4, 5], [10, 15, 45, 50, 60]))
    # 打乱某个序列，从python3.6新增的方法
    list_test = [2, 3, 4, 5, 6]
    random.shuffle(list_test)
    print(list_test)
    # 取样，从某个列表中，随机选择若干个元素
    print(random.sample([1, 2, 3, 4, 5, 6, 7], k=3))


def test_seed():
    """
     验证random的状态
    :return:
    """
    # 验证seed
    random.seed(1)
    print(random.randrange(1000))
    random.seed(1)
    print(random.randrange(1000))
    # 验证random的状态
    state = random.getstate()
    print(random.randrange(1000))
    print(random.randrange(1000))
    random.setstate(state)
    print(random.randrange(1000))


def test_math_distribution():
    """
    验证数学分布
    :return:
    """
    print(random.triangular(0, 9, 7))
    for i in range(10000):
        step = str(round(random.triangular(0, 9, 7)))
        print(step)
        counter.update(step)
    print(counter)

    print("*" * 24)

    counter.clear()
    # 指数分布
    for i in range(10000):
        step = str(round(random.expovariate(1)))
        counter.update(step)

    print(counter)

    print("*" * 24)

    counter.clear()
    for i in range(10000):
        step = str(round(random.gammavariate(9, 0.5)))
        counter.update(step)

    print(counter)
    print("*" * 24)

    counter.clear()
    for i in range(10000):
        step = str(round(random.gauss(5, 1)))
        counter.update(step)

    print(counter)
    print("*" * 24)

    counter.clear()
    for i in range(10000):
        step = str(round(random.vonmisesvariate(3.14, 2)))
        counter.update(step)

    print(counter)
    print("*" * 24)

    counter.clear()
    for i in range(10000):
        step = str(round(random.paretovariate(2)))
        counter.update(step)

    print(counter)
    print("*" * 24)

    counter.clear()
    for i in range(10000):
        step = str(round(random.weibullvariate(1, 5) * 5))
        counter.update(step)

    print(counter)
    print("*" * 24)


if __name__ == '__main__':
    test_seed()
