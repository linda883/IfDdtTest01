import unittest
from ddt import ddt,data,unpack
import csv
import requests
import json

def get_data(file_name):
    rows=[]
    data_file =open(file_name,'r')
    reader = csv.reader(data_file)
    next(reader,None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class testDdt_csv_json(unittest.TestCase):
    @data(*get_data(r'test_data.csv'))
    @unpack
    def test_get_json(self,value):

        data = json.loads(value)
        print(type(data))
        url='https://reqres.in/api/users'
        req = requests.post(url=url,data=data)
        print(req.json())

