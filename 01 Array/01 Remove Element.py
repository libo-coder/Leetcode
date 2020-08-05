# coding=utf-8
"""
在一个数组里面移除指定的 Value，并且返回新的数组长度。注意不能创建新的数组
方法：􏱿􏰭使用两个游标 i，j，遍历数组，如果碰到了 value，使用 j 记录位置，同时递增 i，直到下一个非 value 出现，将此时 i 对应的值复制到 j 的位置上，
     增加 j，重复上述过程直到遍历结束，此时 j 就是新的数组长度。
"""
def remove_element(A, value):
    j = 0
    n = len(A)
    for i in range(n):
        if A[i] == value:
            continue
        A[j] = A[i]
        j += 1
    return j

if __name__ == '__main__':
    A = [1, 2, 2, 3, 2, 4]
    new_l = remove_element(A, 2)
    print(new_l)



