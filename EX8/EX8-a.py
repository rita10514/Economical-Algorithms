import random
import math

def arrangement (l,subgroups):
	s=''
	for i in l:
		s=s+subgroups[i]
	return s	

#a
def Shapley (costs):
	num_of_players = int(math.log(len(costs))/math.log(2))
	l = [x+1 for x in range(num_of_players)]
	subgroups = list(costs.keys())
	MC=[0]*num_of_players
	SV=[0]*num_of_players
	for i in range(len(costs)*10):
		random.shuffle(l)
		print('__________')
		print("the arrangement is: " + arrangement(l,subgroups))
		MC[l[0]-1] = costs[subgroups[l[0]]]
		SV[l[0]-1] = SV[l[0]-1] + MC[l[0]-1]
		s=subgroups[l[0]]
		for j in range (1,num_of_players):	
			s=s+str(subgroups[l[j]])
			MC[l[j]-1] = costs[''.join(sorted(s))] - costs[''.join(sorted(s[:-1]))]
			if j==num_of_players-1 : print("the Marginal Cost in alpabetical order is: " +str(MC))
			SV[l[j]-1] = SV[l[j]-1] + MC[l[j]-1]
		print('_________')	
		print("the sum of the Marginal Cost of each in alphbetical order is: "+str(SV))	
		s=''
	print("")		
	SV = [ x/(len(costs)*10) for x in SV ]
	return SV		

#b	- the result is very simular to the example	
costs = {'0' : 0, 'A' : 10, 'B' : 15, 'C' : 25, 'AB' : 20, 'AC' : 29, 'BC' : 35, 'ABC' : 37}
#NOTE : the input should be sordet by the size of the group in incresing order and each group in an alphapetival order.
#the numbers were taken from the exel example "Shapley Moduler"
print("the Shapley values in alpabetical order is: "+str(Shapley(costs)))
