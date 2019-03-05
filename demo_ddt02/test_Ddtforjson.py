import unittest2
import requests
from ddt import ddt,file_data,unpack
'''
在测试类上使用@ddt装饰符
测试方法上使用@data装饰符
@data装饰符把参数当作测试数据，参数可以是单个值、列表、元组、字典
'''
'''
{
    "name": "morpheus",
    "job": "leader"
}
'''
@ddt
class TestDdtForJson(unittest2.TestCase):

    @file_data('test_data_01.json')
    def test_Interface06(self, **value1):
        print(value1)
        print(type(value1))
        req = requests.post(url='https://reqres.in/api/users',json=value1)
        #
        print(req.json())
        # self.assertEqual(value2, value1 + 1)


if __name__ == '__main__':
    unittest2.main(verbosity=2)
