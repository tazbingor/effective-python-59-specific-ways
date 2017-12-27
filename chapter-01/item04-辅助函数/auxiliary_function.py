#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/28 上午1:00
# @Author  : Aries
# @Site    : 
# @File    : auxiliary_function.py
# @Software: PyCharm
'''
使用辅助函数来取代复杂表达式
    1. 使用if/else表达式
    2. 封装成辅助函数
    3. 函数式编程
总结:
    有时候写程序时特别复杂的罗辑没有必要挤在一行写,此种托大的操作在python中没有太大的意义,在团队开发中要的是简洁明了的代码


'''


# 最简单的封装成函数
def add(num1, num2):
    return num1 + num2


# 或者方便点,写在一行
def mult(x, y): return x * y


# if/else表达式
def max(num1, num2):
    if num1 > num2:
        return True
    else:  # 此处也可以不需要else
        return False


# 更简洁的函数式编程
func_add = lambda num1, num2: num1 + num2
func_mult = lambda x, y: x * y
func_max = lambda num1, num2: True if num1 > num2 else False

if __name__ == '__main__':
    print(func_add(4, 4))  # 8
    print(func_mult(9, 9))  # 81
    print(func_max(81, 8))  # True
