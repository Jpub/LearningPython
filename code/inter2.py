def intersect(*args):
    res = []
    for x in args[0]:                  # Scan first sequence
        if x in res: continue          # Skip duplicates
        for other in args[1:]:         # For all other args
            if x not in other: break   # Item in each one?
        else:                          # No: break out of loop
            res.append(x)              # Yes: add items to end
    return res

def union(*args):
    res = []
    for seq in args:                   # For all args
        for x in seq:                  # For all nodes
            if not x in res:
                res.append(x)          # Add new items to result
    return res
