def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def split(list):
    if len(list) == 1:
        return list
    mdl = len(list)//2
    rg = []
    lf = []
    for i in range(len(list)):
        if i < mdl:
            lf.append(list[i])
        else:
            rg.append(list[i])
    rg = split(rg)
    lf = split(lf)
    return merge(lf, rg)


print(split([5, 2, 9, 6, 0, 3, 4, 1, 2]))
