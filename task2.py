total = 0
for my_no in range(100, 500):
  if (my_no %2)==0:
   total += my_no
print (total)
	

++++++++++++++++++++++++++++
bonus
+++++++++++++++++++++++++++++
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def bonus (r):
    gop = []
    for p in r:
        if type(p) == str:
            gop.append(p.capitalize())
        else:
            gop.append(capitalize_all(p))
    return gop

r = ['hi',['buy']]
print (bonus(r) == ['Hi',['Buy']])
print (capitalize_all(['hello']) == ['Hello'])