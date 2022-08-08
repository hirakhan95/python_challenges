
def word_count(lst):
    res = {}
    for i in lst:
        if i not in res:
            res[i] = 1
        else:
            res[i] += 1
    return res


def frequency_more_than_num(lst, num):
    frequency = word_count(lst)
    temp = set()
    for i in frequency:
        if frequency[i] >= num:
            temp.add(i)
    return temp



#print(frequency_more_than_num(['a', 'b', 'b', 'b', 'd', 'd', 'c', 'd', 'd', 'd', 'd', 'c'], 2))


#print(word_count(["cow", "pig", "cow", "cow", 'horse', 'pig']) )#== {'pig', 'cows'}
# assert pluralize(["cow", "pig", "cow", "cow"]) == {"cows", "pig"}
# assert pluralize(["table", "table", "table"]) == {"tables"}
# assert pluralize(["chair", "pencil", "arm"]) == {"chair", "pencil", "arm"}
# assert pluralize(["list"]) == {"list"}
# assert pluralize(["set", "set", "tuple", "tuple", "string", "string", "string", "string", "integer"]) == {"sets",
#                                                                                                           "tuples",
#                                                                                                           "strings",
#                                                                                                           "integer"}
