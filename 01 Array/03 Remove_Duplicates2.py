# coding=utf-8
"""
在一个排好序的数组中删除重复的元素。但是最多可以允许两次重复元素存在
方法：相比与 02，只需要增加一个计数器即可
"""
def remove_duplicates(a):
    n = len(a)
    if n == 0:
        return
    j = 0
    num = 0
    for i in range(n):
        if a[i] == a[j]:
            num += 1
            if num < 2:
                j += 1
                a[j] = a[i]
            continue
        else:
            j += 1
            a[j] = a[i]
            num = 0
    return j + 1


if __name__ == '__main__':
    a = [1, 1, 2, 2, 2, 2, 2, 3, 4]
    new_l = remove_duplicates(a)
    print(new_l)
