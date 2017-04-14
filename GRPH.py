import sys

args={1: "FASTA FILE", 2: "Subseq Len"}

def checkArgs(usrargs):
  import sys
  count = len(args)
  for i in range(1,count+1):
    try:
      usrargs[i] = sys.argv[i]
    except:
      sys.exit("Please Provide a " + usrargs[i])
  return usrargs
  

def fastaParser (fasta_file_name):
  import re
  id = ''
  fasta = {}
  with open (fasta_file_name , 'r') as FASTA:
    for line in FASTA:
      line = line.rstrip()
      header = re.match("^>(\S+)\s*\w*",line)
      if header:
        id = header.group(1)
      else:
        if id in fasta:
          fasta[id] += line
        else:
          fasta[id] = line
    return fasta

args=checkArgs(args)
seqs=fastaParser(args[1])

k=int(args[2])
prefixes={}
suffixes={}
for id in seqs:
  seq = seqs[id]
  prefix=seq[:k]
  suffix=seq[-k:]
  if prefix not in prefixes:
    prefixes[prefix]=[]
  if id not in prefixes[prefix]:
    prefixes[prefix].append(id)
  else:
    prefixes[prefix].append(id)

  if suffix not in suffixes:
    suffixes[suffix]=[]
  if id not in suffixes[suffix]:
    suffixes[suffix].append(id)
  else:
    suffixes[suffix].append(id)


for pattern in suffixes:
  suffix_ids = suffixes[pattern]
  prefix_ids = []
  if pattern in prefixes:
    prefix_ids = prefixes[pattern]
  for i in suffix_ids:
    for j in prefix_ids:
      if i != j:
        print i + ' ' + j
