'''
1打开浏览器，输入首页地址，这个所有用例之前执行def
2--10定位元素执行操作测试用例
11结束，关闭浏览器
yield 是调用第一次给返回结果，第二次open执行它下面的语句返回

'''
import pytest

@pytest.fixture(scope="module")
def open():
    print("打开浏览器，输入首页地址")

    yield

    print("结束，关闭浏览器")

def test_s8(open):
    print('输入用户名，密码，登陆')


def test_s9(open):
    print('浏览网页查询数据')

if __name__ == '__main__':
    pytest.main