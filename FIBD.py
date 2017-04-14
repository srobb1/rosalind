import sys

months = int(sys.argv[1])
death = int(sys.argv[2])
litter = 1 


def die(rabbitlist):
  dead=rabbitlist.pop(0)
  return dead


rabbits=[]
last_month_mature=0
last_month_young=0
## we start with 1 pair of babies
(young,mature,new_rabbits)=(0,0,1)
for i in range(months):
  month = i + 1

  ## new babies only come from last months mature rabbits
  if last_month_mature > 0:
    new_rabbits = last_month_mature * litter
  
  ## young rabbits are any new rabbits
  young = new_rabbits 

  ## mature rabbits are any mature from last month plus any young from last month
  mature = last_month_mature + last_month_young

  ## total rabbit paris is any young + any mature pairs

  rabbits.append(young)
  dead=0
  if month > death:
    dead=die(rabbits)
  
  mature = mature - dead
  total_rabbit_pairs = young + mature 
  

  print ("month:" + str(month) + ' = ' + str(total_rabbit_pairs) + " pairs" )



  ## reset counters for end of this month
  last_month_young = young
  last_month_mature = mature
  new_rabbits = 0 ## new_rabbits have been counted as young


