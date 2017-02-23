import sys
import re


### functions ####
'''
translate

'''
def justComplement(dna):
  strand_1 = "ATGCatgc"
  strand_2 = "TACGtacg"
  complementation = dna.maketrans(strand_1, strand_2)
  return (dna.translate(complementation))

def justReverse(dna):
  reverse=dna[::-1]
  return reverse

'''
take a dna string and reverse complements it
args dna
returns reverse complment
'''
def reverseComplement(dna):
  reverse=dna[::-1]
  rev_comp=''
  translate = {'A' : "T" , "T" : "A" , "C" : "G" , "G" : "C"}
  for nt in reverse:
    if nt in translate:
      rev_comp = rev_comp + translate[nt]
  return rev_comp
######################

filename=''
try:
  filename=sys.argv[1]
except:
  print("please supply a fasta file name")

seqs={}
id=''
with open(filename,"r") as file:
  for line in file:
    line=line.rstrip()
    header = re.search('^>(\S+)\s*(.*)',line)
    if re.match('^\s*$',line) is not None:
      continue
    elif header:
      id=header.group(1)
    else:
      if id not in seqs:
        seqs[id]=line
      else:
        seqs[id] + line

for id in seqs:
  print(id + ': ' + seqs[id])
  print(id + ' revcomp_1 : ' + reverseComplement(seqs[id]))
  print(id + ' revcomp_2 : ' + justComplement(justReverse(seqs[id])))

