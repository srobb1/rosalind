import sys
import re
#import operator

### functions
'''
calculate GC content
args: dna string
returns: GC content float 
'''
def calculateGC(dna):
  DNA=dna.upper()
  GCcount = DNA.count('G')
  GCcount += DNA.count('C')
  DNAlen = len(DNA)
  percentGC = (GCcount/DNAlen)*100
  return percentGC

#######

userfile=''
try:
  len(sys.argv)>1 
except SystemExit:
  print("Please Provide a fasta file")
else:
  userfile=sys.argv[1]

seqs={}
id='';
with open(userfile,"r") as file:
  for line in file:
    line=line.rstrip()
    header = re.match('^>(\S+)\s*.*',line)
    if header:
      id=header.group(1)
    else:
       try:
         seqs[id]+=line
       except:
         seqs[id]=line

GC={};
for id in seqs:
    GCcontent = calculateGC(seqs[id])
    GC[id]=GCcontent

maxGC_id = max(GC, key=GC.get) 
print (maxGC_id + "\n" + str(GC[maxGC_id]))

