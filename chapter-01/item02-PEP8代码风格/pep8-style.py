#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 上午12:12
# @Author  : Aries
# @Site    : 
# @File    : pep8-style.py
# @Software: PyCharm
'''
编码时,请遵循PEP8代码风格

1. 空白
    1.1 不使用tab制表符,使用space空格代表缩进
    1.2 和语法相关的每一层缩进都用4个空格表示
    1.3 每行字符数小于70
    1.4 多行长表达式,每行多上一行4个空格
    1.5 在同一类中,各个方法之间使用一个空行分开
    1.6 函数与类使用两个空行分开
    1.7 诸如调用函数,使用关键字参数等情况下,不要在两旁添加空格
    1.8 变量赋值时,符号左右两侧各添加一个空格

2. 命名
    2.1 函数,变量,属性均应使用小写字母,单词间用下划线相连
    2.2 受保护的实例属性应以单下划线开头
    2.3 私有实例属性以双下划线开头
    2.4 模块级别的常量,使用 大写字母 + 下划线 来命名
    2.5 类中的实例方法,应将收个参数命名为self,代表对象自身
    2.6 类方法的首个参数,应命名为cls,代表该类自身

3. 表达式及语句
    3.1 切莫将否定语句放在表达式最前面
    3.2 尽量不要通过检测容器的长度来判断容器是否为空,可通过 if not 容器名 的方式书写
    3.3 不要一行中写多种复合语句,应分行书写
    3.4 import语句放在文件开头
    3.5 引入模块时应引入绝对名称
    3.6 相对名称的正确写法 from.import 模块名
    3.7 文件中引入模块的顺序为: 标准库 --> 第三方库 --> 自定义库

'''
from timeit import time  # 3.5
from . import re  # 3.6


def is_empty(alist):
    assert isinstance(alist, list)

    if alist:
        return True
    return False


def main():
    # 3.2
    temp_list = [1, 2, 3]
    print(is_empty(temp_list))  # True
    temp_list = []
    print(is_empty(temp_list))  # False


if __name__ == '__main__':
    main()
