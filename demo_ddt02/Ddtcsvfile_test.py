import unittest
from ddt import ddt,data,unpack
import csv

def get_data(file_name):
    '''
   文件--操作文件（读）--操作第一行，第N行
# 创建一个列表
  rows = []
# 打开一个csv文件，文件名通过参数传进来
  data_file = open(file_name, "r")
# 建立一个csv的读的工具，将文件读进来
  reader = csv23.reader(data_file)
# 跳过第一行的头，头有格式信息，这个头可以是参数名
  next(reader, None)
 # 将reader中的东西读到row中，循环多次
  for row in reader:
将每个row的东西追加到此前定义 rows列表中
  rows.append(row)   #
将读到所有信息以列表形式返回待用
  return rows    #
    '''

    rows=[]
    data_file =open(file_name,'r')
    reader = csv.reader(data_file)
    next(reader,None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class TestForJson2(unittest.TestCase):
    @data(*get_data(r'test_data.csv'))
    def test_get_json(self,value):
        print(value)
