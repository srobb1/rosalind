import sys
import re


try:
  userfile=sys.argv[1]
except:
  sys.exit("provide fasta")

id=''
seqs={}
with open(userfile,'r') as f:
  for line in f:
    line=line.rstrip()
    header = re.match("^>(\S+)\s*.*",line)
    if header:
      id=header.group(1)
    else:
      if id in seqs:
        seqs[id] += line
      else:
        seqs[id] = line

translation = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA *      CAA Q      AAA K      GAA E
UAG *      CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA *      CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""

translation_list = translation.split()
translate = {}
codon=''
for each in range(len(translation_list)):
  if each%2 == 0:
    codon = translation_list[each]
  else:
    translate[codon]=translation_list[each]

####### translate #####
'''
translate a sequence into aminoacids
args string of RNA sequence
returns string of aminoacids
'''
def do_translate(RNA):
  aminoacids=''
  for i in range(0, len(RNA), 3):
    codon = RNA[i:i+3] 
    aminoacids += translate[codon]

  return aminoacids


############

for id in seqs:
  seq = seqs[id]
  print id
  peptide=do_translate(seq)
  print peptide
