def clone(lst):
    res = lst.copy()
    res.append(lst)
    return res


print(clone([1, 1]))
print(clone(["a", "b", "c"]))
print(clone([]), [[]])
