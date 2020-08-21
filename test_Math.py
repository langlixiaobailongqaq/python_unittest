"""对Math类进行单元测试"""
from calculator import Math  # 导入自定义类
import unittest              # 导入unittest模块

class TestMath(unittest.TestCase):  # 测试类
	def setUp(self):                # 测试前环境的准备
		print("test start")

	def test_add(self):           # 测试方法
		j = Math(5, 10)
		self.assertAlmostEqual(j.add(), 15)  # 断言验证结果是否为15
		print("add")

	def test_add1(self):
		j = Math(5, 10)
		self.assertNotEqual(j.add(), 12)  # 断言结果不等于12

	def test_assertTrue(self):
		j = Math(5, 10)
		self.assertTrue(j.add() > 10)  # 判断结果是否大于10

	def test_assertIn(self):
		self.assertIn("a", "a, b, c, d")  # 判断a是否在b里面
		# self.assertIn("a", "b, c, d")

	def test_assetIs(self):
		self.assertIs("abc", "abc")  # a是否跟b一样

	def tearDown(self):                    # 测试后环境的还原
		print("test end")

class Test_sub(unittest.TestCase):
	def setUp(self):
		print("test start")

	def test_sub(self):
		i = Math(8, 8)
		self.assertEqual(i.sub(), 0)
		print("sub")

	def test_sub1(self):
		i = Math(5, 3)
		self.assertEqual(i.sub(), 2)
		print("sub1")

	def tearDown(self):
		print("test end")




if __name__ == '__main__':
	suit = unittest.TestSuite()   # 整合测试用例
	suit.addTest(TestMath("test_add"))
	# suit.addTest(TestMath("test_add1"))
	# suit.addTest(TestMath("test_assertTrue"))
	# suit.addTest(TestMath("test_assertIn"))
	# suit.addTest(TestMath("test_assetIs"))
	suit.addTest(Test_sub("test_sub"))

	runner = unittest.TextTestRunner()  # 用来执行测试用例
	runner.run(suit)

