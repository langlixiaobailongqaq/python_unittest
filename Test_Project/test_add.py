"""
加法测试用例

"""
from Test_Project.calculator import *
from Test_Project.StartEnd import *

class Test_add(Setup_tearDown):
	def test_add(self):
		i = Count(5, 5)
		self.assertEqual(i.add(), 10)

	def test_add1(self):
		i = Count(8, 8)
		self.assertEqual(i.add(), 16)

