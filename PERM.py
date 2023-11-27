from itertools import permutations

def permutation_count_and_list(n): #generate the permutations as a whole and store them
    all_perms = permutations(range(1, n+1))
    permutations_list = list(all_perms)
    
    total_permutations = len(permutations_list)
    return total_permutations, permutations_list
n = 7
total, perms = permutation_count_and_list(n)
print(total)
for perm in perms:
    print(' '.join(map(str, perm)))
