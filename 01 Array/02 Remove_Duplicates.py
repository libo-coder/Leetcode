# coding=utf-8
"""
在一个排好序的数组中删除重复的元素。
方法：􏱿􏰭对于一个排好序的数组，a[n+1] >= a[n]；同样使用两个游标来处理，假设现在 i = j + 1，如果 a[i] == a[j]，那么递增 i，直到 a[i] != a[j]
     这时候再设置 a[j+1] = a[i]，同时递增 i, j ，重复直到遍历结束
"""
def remove_dulpicates(a):
    n = len(a)
    if n == 0:
        return
    j = 0
    for i in range(n):
        if a[i] == a[j]:
            continue
        a[j+1] = a[i]
        j += 1
    return j + 1


if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 4]
    new_l = remove_dulpicates(a)
    print(new_l)