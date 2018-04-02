def Karmarkar_Karp_algo(lst):
	''' Takes a list of numbers, and finds a possible residue of a number partition that
	 	switch some positive numbers to negative, and takes the sum of the new set
	'''

	if len(lst) == 1:
		return lst[0]

	lst.sort(reverse = True)

	i = 0
	
	while i < len(lst) - 1:
		#This loop goes throught the sorted list, and calculates residual
		residue = abs(lst[i] - lst[i+1])
		lst[i] = residue
		lst[i + 1] = 0
		i += 2

	j = 0
	new_lst = []
	while j < len(lst):
		#Puts all the residuals into a new list that the function will call
		#Skips over the zeros since we know where each placement is
		new_lst += [lst[j]]
		j += 2

	return Karmarkar_Karp_algo(new_lst)



print(Karmarkar_Karp_algo([10,8,7,6,5]))
print(Karmarkar_Karp_algo([1,2,1,2,1,3]))
print(Karmarkar_Karp_algo([10,7,4,4]))