# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
#      输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
#      输出：7 -> 0 -> 8
#      原因：342 + 465 = 807

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, list1, list2):
        carry = 0  # 记录是否需要增加新节点，或在链表下一个节点是否需要加1，同时记录链表同级节点的和
        res = pre = ListNode(0)  # 这里的执行顺序是res = ListNode(0), pre = res

        while (list1 or list2 or carry != 0):
            # 判断list1是否有值
            if list1:
                carry += list1.val
                list1 = list1.next
            # 判断list2是否有值
            if list2:
                carry += list2.val
                list2 = list2.next

            # carry有同级节点的和
            # divmod返回商与余数的元组，拆包为carry和val
            # carry有值的话需要增加新节点，或在链表下一个节点需要加1,在循环中会用到
            carry, val = divmod(carry, 10)

            pre.next = pre = ListNode(val)

        return res.next


if __name__ == '__main__':
    sol = Solution()  # 创建对象
    # 定义 list1 链表
    list1 = ListNode(2)
    list1.next = list11 = ListNode(4)
    list11.next = list12 = ListNode(5)

    # 定义list2链表
    list2 = ListNode(5)
    list2.next = list21 = ListNode(6)
    list21.next = list22 = ListNode(4)

    res = sol.addTwoNumbers(list1, list2)

    while res:
        print(res.val)
        res = res.next