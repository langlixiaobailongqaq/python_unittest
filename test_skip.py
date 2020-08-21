"""
	一.跳过测试与预期失败

概要：
	unittest.skip()     直接跳过测试
	unittest.skipif()   条件为真，跳过测试
	unittest.skipUnless  条件为假，跳过测试
	unittest.expectedFailure    预期设置失败

	二.@staticmethod（静态方法）和@classmethod（类方法）
一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。
而使用@staticmethod或@classmethod，就可以不需要实例化，直接通过类名就可以实现调用
使用：直接类名.方法名()来调用。
"""

import unittest

class Test1(unittest.TestCase):
	@classmethod
	def setUpClass(cls):    # 必须有cls参数     #这里第一个参数是cls， 表示调用当前的类名
		print("Class module start test >>>>")

	@unittest.skipIf(4 > 3, "skip Test_d")
	def test_c(self):
		print("c")

	@unittest.skipUnless(1 < 0, "skip test_b")
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

