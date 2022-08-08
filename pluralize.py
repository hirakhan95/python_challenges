def pluralize(lst):
    uniques = []
    repeats = []

    for i in lst:
        if i not in uniques:
            uniques.append(i)
        else:
            repeats.append(i)
    res = set()
    for item in uniques:
        if item in repeats:
            item = item + 's'
            res.add(item)
        else:
            res.add(item)
    return res


assert pluralize(["cow", "pig", "cow", "cow"]) == {'pig', 'cows'}
assert pluralize(["cow", "pig", "cow", "cow"]) == {"cows", "pig"}
assert pluralize(["table", "table", "table"]) == {"tables"}
assert pluralize(["chair", "pencil", "arm"]) == {"chair", "pencil", "arm"}
assert pluralize(["list"]) == {"list"}
assert pluralize(["set", "set", "tuple", "tuple", "string", "string", "string", "string", "integer"]) == {"sets",
                                                                                                          "tuples",
                                                                                                          "strings",
                                                                                                          "integer"}
