# -*- coding:utf-8 -*-

"""测试日志输出"""
import time,os,sys,logging
import unittest


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..')  # 返回脚本的路径
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log_test.log',
                    filemode='w')
logger = logging.getLogger()

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*py')

class MyTest(unittest.TestCase):  # 继承unittest.TestCase

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('执行用例开始')

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('执行用例结束')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
