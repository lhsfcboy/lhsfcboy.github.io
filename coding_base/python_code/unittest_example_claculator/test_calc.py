#! /usr/bin/env python
#  coding:utf8

import unittest
from calc import Calculator


class Test_Calc_add(unittest.TestCase):

    # 加算テスト
    def test_add(self):
        print('Test add(self, num1, num2) ')
        calc = Calculator()
        result = calc.add(10, 20)

        self.assertEqual(result, 30, 'Match expected value')

    # 減算テスト
    def test_sub(self):
        print('Test sub(self, num1, num2) ')
        calc = Calculator()
        result = calc.sub(20, 6)

        self.assertEqual(result, 14, 'Match expected value')

    # 乗算テスト
    def test_mul(self):
        print('Test mul(self, num1, num2) ')
        calc = Calculator()
        result = calc.mul(3, 6)

        self.assertEqual(result, 18, 'Match expected value')

    # 除算テスト
    def test_div(self):
        print('Test div(self, num1, num2) ')
        calc = Calculator()
        result = calc.div(20, 5)

        self.assertEqual(result, 4, 'Match expected value')


if __name__ == '__main__':
    unittest.main()

