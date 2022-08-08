import math

def divisible_by_b(a, b):
    # logic 1
    # for i in range(2, 10000):
    #     temp = b * i
    #     if temp > a:
    #         return temp

    # logic 2
    # division = a / b
    # temp = math.ceil(division)
    # return temp * b

    # logic 3
    for i in range(a+1, 100000000):
        if i % b == 0:
            return i



# print(divisible_by_b(1001, 1000), 2000)

print(divisible_by_b(17, 8), 24)
print(divisible_by_b(98, 3), 99)
print(divisible_by_b(14, 11), 22)
print(divisible_by_b(11, 8), 16)
print(divisible_by_b(450, 36), 468)
print(divisible_by_b(1019, 13), 1027)

