"""
	跳过测试与预期失败

概要：
	unittest.skip()     直接跳过测试
	unittest.skipif()   条件为真，跳过测试
	unittest.skipUnless  条件为假，跳过测试
	unittest.expectedFailure    预期设置失败

"""

import unittest

class Test1(unittest.TestCase):
	def setUp(self):
		pass

	@unittest.skipIf(4 > 3, "skip Test_d")
	def test_c(self):
		print("c")

	@unittest.skipUnless(1 < 0,"skip test_b")
	def test_b(self):
		print("b")

	def tearDown(self):
		pass

class Test2(unittest.TestCase):
	def setUp(self):
		pass

	def test_d(self):
		print("d")

	@unittest.expectedFailure
	def test_a(self):
		print("a")

