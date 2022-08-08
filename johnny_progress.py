
def progress_days(runs):
    miles = 0
    num = 0
    for i in runs:
        if runs[num] < runs[num + 1]:
            miles = miles + 1

        else:
            miles = 0
    return miles






print(progress_days([3, 4, 1, 2])) # 2
# There are two progress days, (3->4) and (1->2)

progress_days([10, 11, 12, 9, 10]) # 3

progress_days([6, 5, 4, 3, 2, 9]) # 1

progress_days([9, 9]) # 0