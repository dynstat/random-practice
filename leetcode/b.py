def isHappy(n: int) -> bool:
    num = n
    sqr_list = [int(i) ** 2 for i in str(num)]
    num = sum(sqr_list)
    list_ = {num}
    while num in list_:
        sqr_list = [int(i) ** 2 for i in str(num)]
        num = sum(sqr_list)
        if num == 1:
            return True
        else:
            if num not in list_:
                list_.add(num)
            else:
                return False
    return False


print(isHappy(2))
