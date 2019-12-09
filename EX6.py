#margarita pinhasov

def choosing_rule(x):
	return x>10
	
def trashold(x):
		return 10

def choices (values):
	ans = []
	for i in values:
		if(choosing_rule(i)):
			ans.append(1)
		else:
			ans.append(0)
	return ans
	
def ismonotonic (values):
		vsort = values.sort()
		c = choices(vsort)
		index1 = -1
		for i in range(len(c)):
			if c[i]==1:
				index1=i
		if index1 == -1: return true		
		for i in range(index1,len(c)):
			if c[i] == 0:
				return false
		return true		
			

def payments (values):
	if ismonotonic(values) == false : print("Error: choosing function is not monotonic")
	ans = []
	for i in values:
		if choices(i) ==1:
			ans.append(trashold(i))
		else:
			ans.append(0)
	return ans		
