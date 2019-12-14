input = [
    'Buttercup must be milked beside Bella'
    , 'Blue must be milked beside Bella'
    , 'Sue must be milked beside Beatrice']

lists = []
# lists = [[1, 2], [2, 3], [4, 5]]

def print_lists(lists):
    for li in lists:
        print(li)
print(lists)

def is_head_of_list(a, li):
    return a == li[0]
def is_tail_of_list(a, li):
    return a == li[-1]
def is_head_or_tail_of_list(a, li):
    return a == li[0] or a == li[-1]

def in_any_position_of_lists(a, lists):
    for li in lists:
        if a in li:
            return True
    return False

def in_lists(a, lists):
    for li in lists:
        if is_head_or_tail_of_list(a, li):
            return True
    return False
in_lists(4, lists)

def insert_into_a_list(a, b, li):
    if a == li[0]:
        li.insert(0, b)
    elif a == li[-1]:
        li.append(b)
    elif b == li[0]:
        li.insert(0, a)
    elif b == li[-1]:
        li.append(a)

def merge_list(a, b, aa, bb):
    if not is_tail_of_list(a, aa):
        aa.reverse()
    if not is_head_of_list(b, bb):
        bb.reverse()
    print(aa, bb, aa + bb)
    return aa + bb

# merge_list(1, 3, [1, 2], [3, 4])
# merge_list(1, 3, [2, 1], [3, 4])
# merge_list(1, 3, [2, 1], [4, 3])
# merge_list(1, 3, [1, 2], [4, 3])

def insert_into_lists(a, b, lists):
    a_in_lists = in_lists(a, lists)
    b_in_lists = in_lists(b, lists)
    one_and_only_one_in_lists = (a_in_lists + b_in_lists) == 1
    if (not a_in_lists) and (not b_in_lists):
        lists.append([a, b])
        return
    elif one_and_only_one_in_lists:
        for li in lists:
            insert_into_a_list(a, b, li)
        return
    # now handle the case that a and b both are already contained in the lists
    aa = []
    bb = []
    for li in lists:
        if is_head_or_tail_of_list(a, li):
            aa = li
        if is_head_or_tail_of_list(b, li):
            bb = li
    lists.remove(aa)
    lists.remove(bb)
    aabb = merge_list(a, b, aa, bb)
    lists.append(aabb)


for line in input:
    words = line.split(' ')
    a = words[0]
    b = words[5]
    print(a, b, lists)
    insert_into_lists(a, b, lists)
    print('inserted', lists)

print_lists(lists)

for name in 'Bessie,Buttercup,Belinda,Beatrice,Bella,Blue,Betsy,Sue'.split(','):
    if not in_any_position_of_lists(name, lists):
        print(name, 'not in', lists)
        lists.append([name])

def sort_list(aa):
    if aa[0] > aa[-1]:
        aa.reverse()


for aa in lists:
    sort_list(aa)

print('PRE-SORTING LISTS')
print_lists(lists)
lists.sort()
print('POST-SORTING LISTS')
print_lists(lists)

for li in lists:
    for a in li:
        print(a)

