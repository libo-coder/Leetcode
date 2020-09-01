# coding=uft-8
"""
@author:libo
"""
def merge(A, m, B, n):
    p, q, k = m-1, n-1, m+n-1
    while p >= 0 and q >= 0:
        if A[p] > B[q]:
            A[k] = A[p]
            p, k = p-1, k-1
        else:
            A[k] = B[q]
            q, k = q-1, k-1
    A[: q+1] = B[:q+1]