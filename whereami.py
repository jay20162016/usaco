input = 'ABCDABC'

N = len(input)

list_of_set = [set() for _ in range(N)] # i'th position holding the set of I-length grams

need_at_least_K = 0


for i in range(N):
    a = input[i]
    print('i', i, 'a', a, list_of_set)
    for letters in range(i + 1):
        sub = input[i - letters:i + 1]
        lensub = len(sub)
        print('\t', 'i', i, 'a', a, 'letters', letters, 'sub', sub, 'lensub', lensub)
        if lensub < need_at_least_K:
            print('skip as lensub', lensub, 'is less than need_at_least_K', need_at_least_K)
            continue
        aset = list_of_set[lensub - 1]
        if sub in aset:
            print('sub', sub, 'already contained in set', aset)
            need_at_least_K = max(need_at_least_K, lensub + 1)
            print('need_at_least_K increased to', need_at_least_K)
        else:
            aset.add(sub)

print(need_at_least_K)
