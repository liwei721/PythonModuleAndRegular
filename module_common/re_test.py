"""
    @author: xuanke
    @time: 2020/1/12
    @function: 对python正则表达式的库re进行验证
"""
import re


def find_and_match():
    """
    验证正则表达式的查找和匹配
    :return:
    """
    target_str = "http://www.baidu.com/query?params1=xiaoming&params2=32"
    # 验证match,从起始位置开始匹配，如果不是起始位置匹配成功，则返回None
    match_result_1 = re.match("www", target_str)
    print(match_result_1)
    match_result_2 = re.match("http", target_str)
    print(match_result_2)
    # 使用groups/group(num)获取表达式

    match_result_3 = re.match(r".*www\.(.*)\.com", target_str)
    print(match_result_3.groupdict())
    print(match_result_3.groups())
    print(match_result_3.group(1))

    # 验证match,从起始位置开始匹配，如果不是起始位置匹配成功，则返回None
    match_result_1 = re.search("www", target_str)
    print(match_result_1)
    match_result_2 = re.search("http", target_str)
    print(match_result_2)
    # 使用groups/group(num)获取表达式

    match_result_3 = re.search(r"www\.(.*)\.com", target_str)
    print(match_result_3.groupdict())
    print(match_result_3.groups())
    print(match_result_3.group(1))

    # findAll
    find_result_1 = re.findall(r"\d+", target_str)
    print(find_result_1)

    # finditer
    find_result_2 = re.finditer(r"\d+", target_str)
    for result in find_result_2:
        print(result.group())


def double(matched):
    num = int(matched.group("number") * 2)
    return str(num * 2)


def find_and_replace():
    """
    检索和替换
    :return:
    """
    # re.sub(pattern, repl, string, count=0, flags=0)
    target_str = "2020-1-12 21:39"
    replace_result = re.sub(r":", "h", target_str)
    print(replace_result)
    print(type(replace_result))

    # repl参数是函数,将字符串中的数字乘以2
    target_str_1 = "12ab34eee"
    replace_result_1 = re.sub(r"(?P<number>\d+)", double, target_str_1)
    print(replace_result_1)


def compile_test():
    """
    正则表达式预编译验证
    :return:
    """
    target_str_1 = "12ab34eee"
    pattern = re.compile(r"\d+")
    result = pattern.findall(target_str_1)
    print(result)


def split_test():
    """
    对分割字符串验证
    :return:
    """
    target_str = "123a345b456c345d"
    pattern = re.compile(r"[a-zA-z]+")
    result = pattern.split(target_str)
    print(result)


if __name__ == '__main__':
    split_test()
