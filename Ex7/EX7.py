import random
from numpy import mean
class Distyibution:
	def __init__(self,values):
		self.values = sorted(values)
		self.len = len(values)
		self.low = self.values[0]
		self.high = self.values[self.len-1]
		self.com = self.commutative()
		
	#this function counts how many values are 
	#under each x when x is between the low and high trasholds
	#this function used by the F(x) function
	def commutative(self):
		ans = {}
		indexj=0
		for i in range(self.low,self.high+1): 
			if str(i) not in ans:
						ans[str(i)]=0
			for j in range(indexj,self.len):
				if self.values[j] < i:
					if j==0:
						ans[str(i)]=1
					else:
						if ans[str(i)] == 0 :
							ans[str(i)]=ans[str(i-1)]+1
						else:
							ans[str(i)]=ans[str(i)]+1										
				else:
					if  j!=0 and ans[str(i-1)] > 0 and ans[str(i)] == 0:
						ans[str(i)]=ans[str(i-1)]
					indexj=j				
					break
		
		return ans
				
	def F(self,x) -> float :		
	
		if x <= self.high and x >= self.low:	
			return self.com[str(x)]/self.len 
		if x < self.low: return 0	
		if x > self.high: return 1	
		
	def r(self,x) ->float:
		x2=x+1
		x1=x-1
		f=(self.F(x2)-self.F(x1))/(x2-x1)
		return x - (1 - self.F(x))/f
		
		
# not part of the assignment - only for testing purpses (comparison with the simulation)		
	def avr(self,x):
		list = []
		for i in self.values:
			if i > x :
				list.append(self.r(i))	
		return sum(list)/self.len	
# ________________________________________	



#values = [int(random.uniform(10, 30)) for i in range(9999)] #singleBuyer_1
values = values = [int(random.uniform(20, 40)) for i in range(9999)] #singleBuyer_2
#values = [random.randint(10, 30) for i in range(9999)]
D = Distyibution(values)
print(D.com)
x=28
print(values)
print("F("+str(x)+")="+str(D.F(x)))
print("r("+str(x)+")="+str(D.r(x)))

#for testing purpses - the resulls are similar to the simulation
#trashold = 15 #singleBuyer_1
trashold = 20 #singleBuyer_2
print("theoretically = " + str(trashold*(1-D.F(trashold))))
print("average of r = "+str(D.avr(trashold)))
