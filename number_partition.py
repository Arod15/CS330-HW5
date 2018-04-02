set = []

def set_table(lst):
	'''Creates the table for the dynamic programming back tracking'''
	max_sum = sum(lst)
	global set
	#Initializes matrix with all 'O'
	M = [['O' for j in range(max_sum + 1)] for i in range(len(lst))]
	
	for i in range(len(lst)):
		#Base case of empty set
		M[i][0] = 'X'

	for i in range(len(lst)):
		#Sets the values of the matrix
		M[i][lst[i]] = 'X'
		print(str(i) + " is " + str(lst[i]))
		if len(set) != 0:
			for x in set:
				# loop through all columns of previous row and make additions
				M[i][lst[i] + x] = 'X'
				print("Let's add " + str(lst[i] + x) + " is " + str(lst[i]))
			set += lst[i]


	print(M)

	

def number_partition(lst):
	'''Dynamic programming solution for Number Partitioning'''
	M = set_table(lst)

set_table([10,7,4,4])
