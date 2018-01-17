nlist=[1,3,45,43,23,[23,423,[23,42],43],43,[5,67,56]]
def sum(a):
    total = 0
    for i in a:
        if isinstance(i, list):
            total += sum(i)
        else:
            total += i
    return total
print (sum(nlist))
