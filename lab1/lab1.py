def ZeroCount(num: int):
    count = int()
    for i in str(num):
        if i == "0":
            count += 1

    return count
