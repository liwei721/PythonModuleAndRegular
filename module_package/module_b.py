"""
    @author: xuanke
    @time: 2020/1/1
    @function: module B
"""
import  sys
sys.path.insert(0, "xxxx")
sys.path.append("xxx")
# import module_package.module_a as module_a
from module_package.module_a import *
from module_package import *

# from module_package import module_a
# from module_package.module_a import test_a
# import module_package

def test_c():
    x = 10
    print("I am test c")
    print(locals())


if __name__ == '__main__':
    test_a()
    test_b()
    print(globals())
    test_c()
    print(sys.path)

