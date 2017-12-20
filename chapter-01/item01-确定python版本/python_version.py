#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17/12/21 上午12:05
# @Author  : Aries
# @Site    : 
# @File    : python_version.py
# @Software: PyCharm
'''
确定python版本
'''
import sys

if __name__ == '__main__':
    print(sys.version_info)
    print(sys.version)
    # sys.version_info(major=3, minor=5, micro=0, releaselevel='final', serial=0)
    # 3.5.0 (v3.5.0:374f501f4567, Sep 12 2015, 11:00:19)
    # [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]

'''
1. 开发项目优先考虑python 3,因为python 2在2018年停止更新
2. 项目中的python版本应该和系统版本一致
'''
