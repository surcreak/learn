
"""
Topic: 动态规划，切割钢管，使得收益最大化
Desc :
    给定一段长度为n的钢条和一个价格表p[i](i=1,2,3,4...n)，
    求切割方案，使得销售收益r[n]最大。
    注意，如果长度为n的钢条价格p[n]足够大，最优解可能是完全不需要切割。
"""

def cut_rod(p, n):
    if n == 0:
        return 0
    q = -999
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n-1))
    return q


if __name__ == '__main__':
    parry = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(cut_rod(parry, 8))