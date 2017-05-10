couples = { 'AAAA' : 17471 , 'AAAa' : 16182 , 'AAaa' : 18976 , 'AaAa' : 16882 , 'Aaaa' : 17913 , 'aaaa' : 16606 }
probs={ 'AAAA' : 1 , 'AAAa' : 1 , 'AAaa' : 1 , 'AaAa' : 0.75 , 'Aaaa' : 0.5 , 'aaaa' : 0 }
offspring_each = 2

dominant_offspring=0;
for gt in couples:
  p=probs[gt]
  dominant_offspring += couples[gt] * (probs[gt] * 1) * offspring_each

print(dominant_offspring)
