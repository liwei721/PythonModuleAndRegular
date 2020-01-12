"""
    @author: xuanke
    @time: 2020/1/11
    @function: 对序列化内容进行验证
"""
import pickle
import json


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_name(self):
        return self.name


def pickle_test():
    """
    对pickle 序列化和反序列化方法进行验证
    :return:
    """
    # 序列化到文件
    data_list = ["mine", 1, "test"]
    print(type(data_list))
    with open("data1", "wb+") as f:
        pickle.dump(data_list, f)

    with open("data1", "rb+") as f:
        load_result = pickle.load(f)
        print("load result ", load_result)

    # 序列化到内存
    data_list_1 = ["mine1mine1", 12, "textdd"]
    dumps_result = pickle.dumps(data_list_1)
    print(type(dumps_result))
    print(dumps_result)

    loads_result = pickle.loads(dumps_result)
    print("loads result is", loads_result)


def json_test():
    """
    用于对json格式方法验证
    :return:
    """
    # 序列化到文件
    data_test = {"name": "xuanke", "age": 30}
    with open("data2", "w+") as f:
        json.dump(data_test, f)
    # 从文件反序列化
    with open("data2", "r+") as f:
        load_result = json.load(f)
        print("load result is ", load_result)

    # 序列化到内存
    dumps_result = json.dumps(data_test)
    print(type(dumps_result))
    print(dumps_result)

    loads_result = json.loads(dumps_result)
    print(loads_result)


def json_class_test():
    """
    尝试序列化一个class
    :return:
    """
    person = Person("xuanke", 30, "M")
    # 使用pickle
    dumps_result = pickle.dumps(person)
    print(dumps_result)
    person_result = pickle.loads(dumps_result)
    print(person_result.name)
    print(person_result.age)

    # TypeError: Object of type Person is not JSON serializable
    # dumps_result = json.dumps(person)
    # print(dumps_result)
    json_dumps_result = json.dumps(person, default=lambda obj: obj.__dict__)
    print(type(json_dumps_result), json_dumps_result)

    json_loads_result = json.loads(json_dumps_result, object_hook=lambda d:Person(d["name"], d["age"], d["sex"]))
    print(type(json_loads_result), json_loads_result.name)


if __name__ == '__main__':
    json_class_test()
