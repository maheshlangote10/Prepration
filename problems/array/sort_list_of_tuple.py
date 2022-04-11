

def sort_list(tup):
    size = len(tup)
    import pdb
    pdb.set_trace()
    for i in range(0,size):
        for j in range(0,size-i-1):
            if tup[j][1] > tup[j+1][1]:
                temp = tup[j]
                tup[j]= tup[j+1]
                tup[j + 1] = temp
    return tup
l1 = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
l2 = [[('452', 10), ('256', 5), ('100', 20), ('135', 15)]]

print(sort_list(l1))
