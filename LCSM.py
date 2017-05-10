import sys

args={1: "FASTA FILE"}

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

sortedIds=[];
for id in sorted(seqs , key=lambda id: len(seqs[id])):
 sortedIds.append(id)


seqA=seqs[sortedIds[0]]
shortest = len(seqA)
#print("seqA: ", seqA);
stop = 0
for i in range(shortest):
  if stop:
    break
  start = 0
  subseq_len = shortest - i
  end =  start + subseq_len  
  #print("start:" , start , " end:", end , "slen:" , subseq_len)
  while end>start and end-start <= subseq_len and end <= shortest: 
    found = 0 
    subseq = seqA[start:end]

    #print("subseq: " , subseq)
    for seqB_ID in range(1,len(sortedIds)):
      seqB=seqs[sortedIds[seqB_ID]]
      #print("start: " , start , "end: ", end,  " seqB_ID: ", seqB_ID , " seqB: " , seqB)
      if seqB.find(subseq) > -1:
        found += 1 
    start = start +1
    end = end + 1

    if found == (len(sortedIds) - 1):
      print("found: " , subseq)
      stop = 1
      break
