li = [1, 2, 3, 4, 5]


# 1+3+5 , 5+3+1
res = 0


def rec(li):
    if not li:
        popped = 0
        return 0
    else:
        popped = li.pop()
    if popped % 2 == 0:
        popped = 0
    return popped + rec(li)


print(rec(li))
