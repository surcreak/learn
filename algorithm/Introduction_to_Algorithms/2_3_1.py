
"""
Topic: 排序
Desc :
    给定一个乱序的数组，求其非递减序列。
"""

import sys, math

"""
    解法1、归并排序
    param a: 要排序的数组
    param p: 排序开始位置
    param r: 排序结束位置
"""
def merge_sort(a, p, r):
    print("p="+repr(p)+";r="+repr(r))
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
    return a

"""
    按序合并两数组
    param a: 要排序的数组
    param p: 第一个数组开始位置
    param q: 第一个数组结束位置，第二个数组开始位置
    param r: 第二个数组结束位置
"""
def merge(a, p, q, r):
    print("p="+repr(p)+";q="+repr(q)+";r="+repr(r))
    n1 = q - p + 1
    n2 = r - q 
    L = [sys.maxsize] * (n1 + 1)
    R = [sys.maxsize] * (n2 + 1)
    for i in range(0, n1):
        L[i] = a[p + i]
    for j in range(0, n2):
        R[j] = a[q + j + 1]
    i = j = 0
    print(L)
    print(R)
    for k in range(p, r + 1):
        if(L[i] <= R[j]):
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
    print(a)
    print("=========================")
    return
    
if __name__ == '__main__':
    a = [8, 4, 5, 7, 1, 4, 6, 2, 33, 11, 22, 10]
    print(a)
    print(merge_sort(a, 0, len(a) - 1))