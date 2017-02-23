dna = raw_input('paste your dna sequence: ')

print(dna)
dna_count={}
for nt in dna:
  if nt in dna_count:
    dna_count[nt] += 1
  else:
     dna_count[nt] = 1

#for nt in sorted(dna_count):
#  print nt + "=" + str(dna_count[nt])

nts = list(sorted(dna_count.keys()))
counts=[dna_count[nt] for nt in nts ]
sep=" "
print sep.join(str(count) for count in counts)
