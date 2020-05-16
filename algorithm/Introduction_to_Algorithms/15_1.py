
"""
Topic: 动态规划，切割钢管，使得收益最大化
Desc :
    给定一段长度为n的钢条和一个价格表p[i](i=1,2,3,4...n)，
    求切割方案，使得销售收益r[n]最大。
    注意，如果长度为n的钢条价格p[n]足够大，最优解可能是完全不需要切割。
"""

"""
    解法1、自顶向下递归，时间复杂度O(2^n)。因为反复求解相同的子问题。
    param p: 价格数组，长度为i的钢条价格为p[i]
    param n: 钢条总长度
"""
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -999
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q

"""
    解法2、带备忘录自顶向下递归，时间复杂度O(n^2)。
    param p: 价格数组，长度为i的钢条价格为p[i]
    param n: 钢条总长度
    param r: 备忘录数组
"""
def memo_cut_rod(p, n):
    r = [-999]*(len(parry) + 1)
    return memo_cut_rod_aux(p, n, r)

def memo_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -999
        for i in range(1, n+1):
            q = max(q, p[i] + memo_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q

"""
    解法3、自底向上递归，时间复杂度O(n^2)。
    param p: 价格数组，长度为i的钢条价格为p[i]
    param n: 钢条总长度
"""
def bottom_up_cut_rod(p, n):
    r = [0] * (len(p) + 1)
    if n == 0:
        return 0
    q = -999
    for j in range(1, n+1):
        for i in range(1, j+1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

"""
    解法4、自底向上递归，时间复杂度O(n^2)。并返回解本身。
    param p: 价格数组，长度为i的钢条价格为p[i]
    param n: 钢条总长度
    param s: 切割解本身
"""
def bottom_up_cut_rod_solution(p, n, s):
    r = [0] * (len(p) + 1)
    if n == 0:
        return 0
    q = -999
    for j in range(1, n+1):
        for i in range(1, j+1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r
    

if __name__ == '__main__':
    parry = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    s = [0] * (len(parry) + 1)
    # print(cut_rod(parry, 3))
    # print(memo_cut_rod(parry, 4))
    # print(bottom_up_cut_rod(parry, 4))
    print(bottom_up_cut_rod_solution(parry, 10, s))
    print(s)