def oddish_or_evenish(num):
    res = []
    for i in str(num):
        splitted_part = int(i)
        res.append(splitted_part)
    res = sum(res)

    if res % 2 == 0:
        return 'Evenish'
    else:
        return 'Oddish'


    # if sum(map(int, str(num))) % 2 == 0:
    #     return 'Evenish'
    # else:
    #     return 'Oddish'


print(oddish_or_evenish(43), "Oddish")
print(oddish_or_evenish(373), "Oddish")
print(oddish_or_evenish(55551), "Oddish")
print(oddish_or_evenish(694), "Oddish")
print(oddish_or_evenish(4433), "Evenish")
print(oddish_or_evenish(11), "Evenish")
print(oddish_or_evenish(211112), "Evenish")
