import random
import math
from itertools import combinations

def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

#a
def shapley (costs):
	num_of_players = int(math.log(len(costs))/math.log(2))
	l = [x+1 for x in range(num_of_players)]
	subgroups = list(costs.keys())
	MC=[0]*num_of_players
	SV=[0]*num_of_players
	for i in range(len(costs)*10):
		random.shuffle(l)
		print('__________')
		print(l)
		MC[l[0]-1] = costs[subgroups[l[0]]]
		SV[l[0]-1] = SV[l[0]-1] + MC[l[0]-1]
		s=subgroups[l[0]]
		for j in range (1,num_of_players):	
			s=s+str(subgroups[l[j]])
			MC[l[j]-1] = costs[''.join(sorted(s))] - costs[''.join(sorted(s[:-1]))]
			if j==2 : print(MC)
			SV[l[j]-1] = SV[l[j]-1] + MC[l[j]-1]
		print('_________')	
		print(SV)	
		s=''	
	SV = [ x/(len(costs)*10) for x in SV ]
	return SV	

#b	- the result is very simular to the example	
#costs = {'0' : 0, 'A' : 10, 'B' : 15, 'C' : 25, 'AB' : 20, 'AC' : 29, 'BC' : 35, 'ABC' : 37}
#NOTE : the input should be sordet by the size of the group in incresing order and each group in an alphapetival order.
#the numbers were taken from the exel example "Shapley Moduler"

runwayportion = ['0A','1A','2A','3A','4A','5A','6A','7A','8A','9A','0B','1B','2B','3B','4B','5B','6B','7B','8B','9B','0C','1C','2C','3C','4C','5C','6C','7C','8C','9C']
sublists = sub_lists(runwayportion)
print(sublists)







#print(shapley(costs))
