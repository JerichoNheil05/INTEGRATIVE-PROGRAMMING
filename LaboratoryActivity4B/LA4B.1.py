# Given sets
aset = {'a', 'b', 'c', 'd', 'g', 'f'}
bset = {'l', 'm', 'o', 'h', 'c', 'b'}
cset = {'c', 'h', 'k', 'i', 'j', 'f', 'd'}

# Dictionary to store results
results = {}

# a. Number of elements in A and B (Union)
results["Number of elements in set A and B:"] = len(aset.union(bset))

# b. Number of elements in B that are not in A and C
results["Number of elements in B that are not in A and C:"] = len(bset.difference(aset.union(cset)))

# c. showing the following using set operations

#Elements in C but not in A [h, i, j, k]
results["\ni."]  = sorted(cset.difference(aset))

#Same elements of set A and C [c, d, f]
results["ii."] = sorted(aset.intersection(cset))

#Elements in A and B, A and C [b, c, f]
results["iii."] = sorted((aset & bset) | (bset & cset))

#Elements that both found in A and C but not in B [d, f]
results["iv."] = sorted(aset.intersection(cset).difference(bset))

#Elements that all the sets have in common [c]
results["v."] = sorted(aset.intersection(bset, cset))

#Elements that only found in B [l, m, o]
results["vi."] = sorted(bset.difference(aset.union(cset)))

# Print the results
for key, value in results.items():
    print(f"{key} {value}")