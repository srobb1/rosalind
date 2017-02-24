import sys
import re

try:
  file=sys.argv[1]
except:
  sys.exit("provide fasta of two equal length DNA strings")

seqs={}
id=''
with open(file,'r') as f:
  for line in f:
    line=line.rstrip()
    header=re.match('>(\S+)\s*.*',line)
    if header:
      id=header.group(1)
    else:
      try:
        seqs[id]+=line
      except:
        seqs[id]=line
ids=list(seqs.keys())
if len(ids)>2:
  sys.exit("fasta must contain 2 seqs of equal length.")
seq1 = seqs[ids[0]]
seq2 = seqs[ids[1]]
mutations=0
for i in range(len(seq1)):
  if seq1[i] != seq2[i]:
    mutations += 1

print(mutations)
