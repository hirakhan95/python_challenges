
def histogram(lst, char):
    temp = []
    for v in lst:
        res = char * v
        temp.append(res)
    var = '\n'.join(temp)
    return var

#print(histogram([2, 4, 5, 6], "o"))
      #'oo\noooo\nooooo\noooooo')
#print(histogram([4, 2] ) )#, "*"), '****\n**')
print(repr(histogram([20, 1, 12], "H")))#, 'HHHHHHHHHHHHHHHHHHHH\nH\nHHHHHHHHHHHH')
# print(histogram([2, 1, 2, 4, 5, 2, 3], "#"), '##\n#\n##\n####\n#####\n##\n###')