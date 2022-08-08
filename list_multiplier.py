def multiply(l):
    length_of_l = len(l)
    res = []
    for i in l:
        temp = [i] * length_of_l
        res.append(temp)
    return res


print(multiply([4, 5]))
