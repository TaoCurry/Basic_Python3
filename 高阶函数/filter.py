def not_empty(s):
    return s and str.strip(s)

l = list(filter(not_empty,['A',' ','C',None,'v',' ']))
print(l)