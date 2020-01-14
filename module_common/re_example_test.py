"""
    @author: xuanke
    @time: 2020/1/14
    @function: python  正则表达式练习题——获取豆瓣电影评分前250
"""
import requests
import re
import json


def write_dict_to_file(dict_item):
    """
    将dict写入文件
    :param dict_item:
    :return:
    """
    with open("move_rank1.txt", "a+", encoding="utf-8") as f:
        json.dump(dict_item, f, ensure_ascii=False)
        f.write("\n")
        f.close()


def get_douban_moive():
    """
    获取豆瓣电影电影
    :return:
    """
    douban_url = "https://movie.douban.com/top250?start={}&filter="
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}

    pattern = re.compile(r'<em class="">(\d+?)</em>.*?src="(.*?)".*?<span class="title">(.*?)</span>'
                         r'.*?<span class="title">(.*?)</span>.*?<span class="other">(.*?)</span>'
                         r'.*?<p class="">(.*?)</p>'
                         r'.*?<span class="rating_num".*?>(.*?)</span>'
                         r'.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>', re.S)
    for i in range(10):
        print(douban_url)
        response = requests.get(douban_url.format(i * 25), headers=headers)
        result_list = pattern.findall(response.text)
        for tuple_item in result_list:
            second_title = re.sub(r"&nbsp;", ' ', tuple_item[3]).strip()
            other_title = re.sub(r"&nbsp;", ' ', tuple_item[4]).strip()
            other_title = re.sub(r"\n", ' ', other_title).strip()
            other_title = re.sub(r"<br>", ' ', other_title).strip()
            describute = re.sub(r"&nbsp;", ' ', tuple_item[5]).strip()
            describute = re.sub(r"<br>", ' ', describute).strip()
            describute = re.sub(r"\n", ' ', describute).strip()
            dict_item = {
                "rank": tuple_item[0],
                "picUrl": tuple_item[1],
                "title": "{}{}{}".format(tuple_item[2], second_title, other_title),
                "desc": describute,
                "score": tuple_item[6],
                "commentNum": tuple_item[7],
                "comment": tuple_item[8]
            }
            write_dict_to_file(dict_item)


if __name__ == '__main__':
    get_douban_moive()
