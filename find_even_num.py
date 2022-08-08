def find_even_nums(num):
    # temp = []
    # for i in range(1, num+1):
    #     if i % 2 == 0:
    #         temp.append(i)
    # return temp

    return list(range(2, num+1, 2))

print(find_even_nums(1))
print(find_even_nums(9))# [2, 4 ,6, 8])
print(find_even_nums(11))#[2, 4 ,6, 8, 10])

