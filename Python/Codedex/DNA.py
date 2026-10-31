dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = input("Enter the codon to search for: ")
item_found = False

for codon in dna_sequence:
    if codon == item_to_find:
        item_found = True
        break

if item_found:
    print(f"Item found: {item_to_find}")
else:
    print(f"Item not found: {item_to_find}")