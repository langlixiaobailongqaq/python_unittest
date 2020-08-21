"""
默认用例执行顺序：
	测试类或测试方法的数字与字母顺序：0-9，A-Z

自定义执行顺序：
	在整合测试用例后面按照自己想要的执行顺序单个去执行用例

	unittest.main()/ suit = unittest.TestSuite()   # 整合测试用例    suit.addTest(TestMath("test_add"))

"""
import unittest


class Test1(unittest.TestCase):
	def setUp(self):
		print("Test1 start")

	def test_c(self):
		print("test_c")

	def test_b(self):
		print("test_b")

	def tearDown(self):
		print("test end")


class Test2(unittest.TestCase):
	def setUp(self):
		print("Test start")

	def test_d(self):
		print("test_d")

	def test_a(self):
		print("test_a")

	def tearDown(self):
		print("Test2 end!")


if __name__ == '__main__':
	unittest.main()