import unittest
from ddt import ddt,data,unpack
'''
在测试类上使用@ddt装饰符
测试方法上使用@data装饰符
@data装饰符把参数当作测试数据，参数可以是单个值、列表、元组、字典
'''
'''

'''
@ddt
class TestDdt(unittest.TestCase):
    # 单个值
    # @unittest.skip
    @data('你好','你','我')

    def test_Interface01(self,value1):
        '''
        这里写接口请求
        '''
        print(value1)
        self.assertEqual('你',value1)

    # 单个列表
    # @unittest.skip
    @data([2],[1])
    @unpack
    def test_Interface02(self, value1):
        '''
        这里写接口请求
        '''
        print(value1)
        self.assertEqual(3, value1 + 1)

    # @unittest.skip
    @data((1,2),(2,3))
    @unpack
    def testInterface03(self, value1,value2):
        '''
        这里写接口请求
        '''
        print(value1,value2)
        self.assertEqual(value2, value1 + 1)


    # @unittest.skip
    @data([2,3],[3,4],[4,5])
    @unpack
    def test_Interface04(self, value1,value2):
        '''
        这里写接口请求
        '''
        print(value1)
        self.assertEqual(value2, value1 + 1)

    # @unittest.skip
    @data(({'num':2},{'name':'linda'}),({'num':3},{'name':'lemed'}))
    # @unpack
    def test_Interface05(self, value1):
        '''
        这里写接口请求
        '''
        print(value1)
        # self.assertEqual(value2, value1 + 1)

    @unpack
    @data({'first':1,'second':2},{'first':3,'second':4})
    def test_show_value(self, second, first):
        print ('value is %s and %s'%(first,second))
        print('case is over.\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)
