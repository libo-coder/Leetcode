# coding=utf-8
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
"""
# def pascal_triangle(numRows):
#     tmp = []
#     for i in range(numRows):


def triangles():
    p = [1]
    while True:
        yield p     # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

