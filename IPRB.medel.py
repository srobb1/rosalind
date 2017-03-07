

##  k+m+n: 
## kk individuals are homozygous dominant for a factor, 
## mm are heterozygous, 
## nn are homozygous recessive.
##
## 2 2 2
##
## kk (2/6) * kk (1/5) * 1   
## kk (2/6) * mm (2/5) * 1
## kk (2/6) * nn (2/5) * 1
## mm (2/6) * kk (2/5) * 1 
## mm (2/6) * mm (1/5) * .75
## mm (2/6) * nn (2/5) * .5
## nn (2/6) * kk (2/5) * 1 
## nn (2/6) * mm (2/5) * .5
## nn (2/6) * nn (1/5) * 0
## 
##
##
##

#(k,m,n)=(2,2,2)
(k,m,n)=(15,28,17) ##0.7353107344632769

def getFreq(genotype,genotypes):
  total = getTotalPool(genotypes)
  count=genotypes[genotype]
  return count/total

def getTotalPool(genotypes):
  total = 0
  for genotype in genotypes:
    total += genotypes[genotype]
  return total

def resetGenotypes():
  genotypes = { 'k':k , 'm':m ,'n':n }
  return genotypes


genotype_freqs={ 'kk':1  , 'km':1 , 'kn':1 ,  'mk':1 , 'mm':0.75,'mn':0.5 , 'nk':1 , 'nm':.5 , 'nn':0  }
genotype_totals = { 'k':k , 'm':m ,'n':n }
genotypes = sorted(list(genotype_totals))
freqs={};
for i in genotypes:
  freq_i = getFreq(i,genotype_totals)
  for j in genotypes:
    genotype_totals[i] = genotype_totals[i] - 1 
    freq_j =  getFreq(j,genotype_totals)
    mates=i+j
    freq_dom=genotype_freqs[mates]
    freq = freq_i * freq_j * freq_dom
    freqs[mates]=freq
    genotype_totals = resetGenotypes()
print(freqs)
print(sum(freqs.values()))


