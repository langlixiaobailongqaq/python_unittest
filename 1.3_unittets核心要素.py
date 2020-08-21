"""
Unittest核心要素：
	1.TestCase：
		一个TestCase的实例就是一个测试用例。什么是测试用例呢？就是一个完整的测试流程，包括测试前准备环境的准备（setUp）,
			执行测试代码（run），以及测试后环境的还原（tearDown）。单元测试（unit test）的本质也就在这里，一个测试用例是
				一个完整的测试单元，通过运行这个测试单元，可以对某一个问题进行验证。
	2.TestSuite：
		而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite。
		TestLoader是用来加载测试用例到TestSuite中的。

	3.TextTestRunner：
		TextTestRunner是用来执行测试用例的，其中的run（）会执行TestSuite/TestCase中的run(result)方法。测试的结果会保存到
			TextTestResult实例中，包括运行了多少测试用例，成功了多少，失败了多少等信息。

	4.Fixture:
		而对一个测试用例环境的搭建和销毁，是一个Fixture

	案例：
		构造一个类Math，包含整数假发运算  calculator.py

"""