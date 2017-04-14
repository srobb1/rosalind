import re
import sys

try:
  user_file=sys.argv[1]
except:
  exit.sys("Provide A FASTA")


id =''
seqs ={}
with open (user_file,'r') as f:
  for line in f:
    line=line.rstrip()
    header = re.match("^>(\S+)\s*\w*",line)
    if header:
      id = header.group(1)
    else:
      if id in seqs:
        seqs[id] += line
      else:
        seqs[id] = line

profile={}
## each seq
for id in seqs:
  seq = seqs[id]
  pos = 0
  ## each nt in seq
  for nt in seq:
    pos+=1
    if pos not in profile:
      profile[pos]={}
    if nt in profile[pos]:
      profile[pos][nt]+=1
    else:
      profile[pos][nt]=1
  
consensus={}
   

for pos in profile:
  maxCount=0
  for nt in profile[pos]:
    count = profile[pos][nt]
    if count > maxCount:
      maxCount = count
      consensus[pos]=nt 

consensusString=''
for pos in consensus:
  consensusString+=consensus[pos]
  
print consensusString

consensusLen = len(consensus)
sep = ' ' 
NTs=['A','C','G','T']
for nt in NTs:
  counts=[]
  count=0
  for i in range(1,consensusLen+1):
    if nt in profile[i]:
      counts.append(str(profile[i][nt]))
    else:
      counts.append(str(0))
  print nt + ": " + sep.join(counts)  

