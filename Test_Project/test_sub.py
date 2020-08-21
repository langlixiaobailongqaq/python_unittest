"""
减法测试用例

"""
from Test_Project.calculator import *
from Test_Project.StartEnd import *

class Test_sub(Setup_tearDown):
	def test_sub(self):
		i = Count(5, 5)
		self.assertEqual(i.sub(), 0)

	def test_sub1(self):
		i = Count(8, 5)
		self.assertEqual(i.sub(), 3)
