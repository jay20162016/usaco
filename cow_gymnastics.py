input = [[4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3]]

import itertools

def get_possible_pairs(alist):
    return set(itertools.combinations(alist, 2))

sets = []
for i in input:
    sets.append(get_possible_pairs(i))

fset = sets[0].intersection(*sets)

print(len(fset))
