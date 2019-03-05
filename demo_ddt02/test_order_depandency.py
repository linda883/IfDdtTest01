import unittest
import pytest

class test_Dep(unittest.TestCase):
    @pytest.mark.run(order=1)
    @pytest.mark.dependency
    def test_01(self):
        print('test01')
        self.assertEqual(4, 1)


    @pytest.mark.dependency(depends=['test_Dep::test_01'])
    def test_02(self):
        print('test02-注册')

    def test_03(self):
        print('test03-登陆')

    def test_04(self):
        print('test04')
        self.assertGreaterEqual(4,1)

