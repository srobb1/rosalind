import re
import sys

file = sys.argv[1]
#print file

dna='';
with open(file, 'r') as file:
  for line in file:
    line=line.rstrip()
    if re.match('^\s*$',line) is not None:
      print "white line"
      continue
    elif re.match('^>',line) is not None:
      continue
    dna+=line;

print(dna)
dna_count={}
for nt in dna:
  if nt in dna_count:
    dna_count[nt] += 1
  else:
     dna_count[nt] = 1

for nt in sorted(dna_count):
  print nt + "=" + str(dna_count[nt])

