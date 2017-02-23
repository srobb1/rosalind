import sys
import re

#### functions ###
''' 
transcribe takes a string of dna a returns rna
arg: dna 
return: rna
'''

def transcribe(dna):
  rna = dna.replace("T", "U")
  return rna
###################

usrfile = sys.argv[1]

seqs={};
id='';
with open(usrfile ,"r") as file:
  for line in file:
    line=line.rstrip()
    header=re.search('^>(\S+)\s*(.*)',line)
    if re.match('^\s*$',line) is not None:
      continue
    elif header:
      id=header.group(1) 
      continue
    if id not in seqs:
      seqs[id] = line
    else:
      seqs[id]+=line;

for id in seqs:
  print id + ' length=' + str(len(seqs[id])) + ' ' + transcribe(seqs[id])


