"""
    @author: xuanke
    @time: 2020/1/13
    @function: 对正则表达式进行验证
"""
import requests
import re
import json


def write_data_to_file(content):
    """
    将数据写入文件中
    :param content:
    :return:
    """
    with open("movie_rank.txt", 'a+', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False)
        f.write("\n")
        f.close()


def get_html_content():
    """
    从html中获取对应图片url和 <a></a>之间的内容
    :return:
    """
    url = "https://movie.douban.com/top250?start={}&filter="
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/69.0.3497.92 Safari/537.36"}
    pattern = re.compile(
        r'<em class="">(\d+)</em>.*?src="(.*?)".*?<span class="title">(.*?)</span>.*?<span class="title">(.*?)</span>'
        r'.*?<span class="other">(.*?)</span>.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>'
        r'.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>', re.S)
    for i in range(1):
        result = requests.get(url.format(i * 25), headers=header)
        match_result = pattern.findall(result.text)
        second_title = ''
        third_title = ''
        describe = ''
        for item_tuple in match_result:
            second_title = re.sub(r'&nbsp;', ' ', item_tuple[3]).strip()
            third_title = re.sub(r'&nbsp;', ' ', item_tuple[4]).strip()
            describe = re.sub(r'&nbsp;', '', item_tuple[5]).strip()
            describe = re.sub(r'\n ', '', describe).strip()
            describe = re.sub(r'<br>', '', describe).strip()
            describe = describe.replace(" ", "")
            item_dict = {
                'rank': item_tuple[0],
                'picUrl': item_tuple[1],
                'title': "{}{}{}".format(item_tuple[2], second_title, third_title),
                'describe': describe,
                'score': item_tuple[6],
                'commentNum': item_tuple[7],
                'comment': item_tuple[8]
            }
            write_data_to_file(item_dict)


def random_every_day():
    """
    每天给我返回一条
    :return:
    """


if __name__ == '__main__':
    get_html_content()
