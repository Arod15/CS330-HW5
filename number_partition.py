def set_table(lst):
	'''Creates the table for the dynamic programming back tracking'''
	max_sum = sum(lst)

	#Initializes matrix with all 'O'
	M = [['O' for j in range(max_sum)] for i in range(len(lst))]
	
	for i in range(len(lst)):
		#Base case of empty set
		M[i][0] = 'X'

	for i in range(len(lst)):
		#Sets the values of the matrix
	print(M)

	

def number_partition(lst):
	'''Dynamic programming solution for Number Partitioning'''
	M = set_table(lst)

set_table([10,7,4,4])