from itertools import permutations

def unique_permutations(s):   
    return set(''.join(p) for p in permutations(s))

string = "yamini"
permutations = unique_permutations(string)
print("All unique permutations:", permutations)
