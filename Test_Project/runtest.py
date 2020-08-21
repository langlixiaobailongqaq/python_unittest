"""
用例执行管理
	使用discover 可以一次调用多个脚本
	test_dir 被测试脚本的路径
	pattern 脚本名称匹配规则
"""

import unittest


test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*py')

# test_dir = "./test_case"
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test* .py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
