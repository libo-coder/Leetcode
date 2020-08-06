# coding=utf-8
"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位，数组中每个元素只存储单个数字。
假设除了整数 0 以外，这个整数不会以 0 开头。
方法：加法进位问题
"""
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    flag = 1
    for i in range(len(digits) - 1, -1, -1):
        if flag == 1:
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] = 0
            else:
                flag = 0
    if flag == 1:
        digits.insert(0, 1)
    return digits