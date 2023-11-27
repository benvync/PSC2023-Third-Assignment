from itertools import product

def ordered_strings(my_alphabet, n):
    all_strings = [''.join(p) for p in product(my_alphabet, repeat=n)]
    sorted_strings = sorted(all_strings, key=lambda s: [my_alphabet.index(c) for c in s])
    return sorted_strings

my_alphabet = ['A', 'C', 'G', 'T']
n = 2

results = ordered_strings(my_alphabet, n)
for s in results:
    print(s)
