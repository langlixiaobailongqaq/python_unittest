"""
用例综合框架管理
	前面测试用例与执行都是写在一个文件，当用例数量不断增加的时候，用例的执行与管理变得非常麻烦，因此需要对用例具体的功能模块来
		使用单独的模块来管理。

案例：Test_Project文件目录下包含4个python文件：
	StartEnd.py———SetUP与TearDown管理
	calculatory.py——加减法运算方法的实现
	test_add.py——加法测试用例
	test_sub.py——减法测试用例
	runtest.py——用例执行管理
"""