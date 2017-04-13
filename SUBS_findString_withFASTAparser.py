import sys
import re

try:
  usr_file = sys.argv[1]
except:
  sys.exit("Provide a FASTA")

try:
  usr_input = sys.argv[2]
except:
  sys.exit("Provide a FASTA and a PATTERN to find in fasta")


id=''
seqs={}

with open (usr_file, 'r') as f:
  for line in f:
    line = line.rstrip()
    header = re.match("^>(\S+)\s*\s*",line)
    if header:
      id = header.group(1)
    else:
      if id in seqs:
        seqs[id] += line
      else:
        seqs[id] = line


MOTIF=sys.argv[2]


def findMotif (STRING, PATTERN, START=0):
  pos = STRING.find(PATTERN,START)
  return pos

for id in seqs:
  DNA=seqs[id]
  pos = 0 
  found=[]
  while (pos >= 0):
    pos = findMotif(DNA, MOTIF, pos)
    if pos > 0:
      pos+=1
      found.append(str(pos))

  sep = ' '
  print id + " " + MOTIF
  print sep.join(found)
