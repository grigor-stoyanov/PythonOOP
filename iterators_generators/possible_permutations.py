def possible_permutations(seq):
    if len(seq) == 0:
        return []
    if len(seq) == 1:
        return [seq]
    l = 0
    for i in range(len(seq)):
        m = seq[i]
        remLst = seq[:i] + seq[i + 1:]
        for p in possible_permutations(remLst):
            l.append([m] + p)
    return l

def possible_permutations(my_list, counter=0):
    global permutations
    permutations = {}
    if counter == len(my_list):
        if not my_list in permutations.values():
            yield my_list
        return
    for i in range(counter, len(my_list)):
        my_list[i], my_list[counter] = my_list[counter], my_list[i]
        permutations[str(my_list)] = (my_list)
        if not my_list in permutations.values():
            yield my_list
        yield from possible_permutations(my_list, counter + 1)
        my_list[i], my_list[counter] = my_list[counter], my_list[i]


[print(n) for n in possible_permutations([1, 2, 3])]
