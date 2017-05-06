# future backtrack version of solver
import copy

class Sudoku():

	def __init__(self, grid):
		self.grid = grid
		self.standard_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

		self.poss_grid = self.build_possible()
		# print self.poss_grid

	# prints out sudoku board
	def print_grid(self):
		for i in range(81):
			print str(self.grid[i]),
			# add a black line every 3 columns
			if (i + 1) % 27 == 0 and (i + 1) != 81:
				print '\n'
			# write every column on new line
			elif (i + 1) % 9 == 0:
				print ''
			# seperate every 3 numbers
			elif (i+1) % 3 == 0:
				print ' ',

	def s_solve(self):
		return self.solve(self.grid, self.poss_grid)

	# solves puzzle
	def solve(self, grid, poss_grid):
		# init variables
		i = 0
		counter = 0
		backtrack = False
		# backtrack = False

		# make copy of lists
		temp_grid = copy.deepcopy(self.grid)
		temp_poss_grid = copy.deepcopy(self.poss_grid)

		# main loop for funciton
		while i < 81:# and counter < 35:
			
		#print counter, i, self.poss_grid[6], temp_poss_grid[6]

			# print i
			# print "i at the start is", i, "",
			# otherwise go through checks
			# if there are values in temp_poss grid
			if len(temp_poss_grid[i]) > 0:

				# lowest value in list becomes test value
				test_value = min(temp_poss_grid[i])

				# if value is valid, place in temp_grid, incriment by 1
				if self.grid[i] != 0:
					temp_grid[i] = self.grid[i]
					if backtrack == True:
						temp_poss_grid[i - 1] = [j for j in self.poss_grid[i  - 1] if j > temp_grid[i - 1]]
						i -= 1
					else:
						i += 1
					# print "hard value, no change, backtracking:", backtrack
				elif self.check_valid(i, temp_grid, test_value):
					backtrack = False
					temp_grid[i] = test_value
					# print "inserting ", test_value, "at ", i
					# print "i was", i,
					i += 1
					# print "add 1, i is now", i


				# if value is not valid, remove from temp_pos_list, do not incriment
				else:
					# print test_value, "was invalid, removing"
					temp_poss_grid[i].remove(test_value)
					# print "no change to i, i is still", i

			# if there are no values in temp_poss_grid, backtracking starts
			else:
				# reset current grid
				temp_grid[i] = 0
				temp_poss_grid[i] = copy.deepcopy(self.poss_grid[i])
				# print "reset current list back to ", temp_poss_grid[i],
				# modify next grid
				#print poss_grid[i - 1], temp_grid[i-1],
				if len(temp_poss_grid[i-1]) != 1:
					temp_poss_grid[i - 1] = [j for j in self.poss_grid[i  - 1] if j > temp_grid[i - 1]]
				# print "previous list is now ", temp_poss_grid[i-1]
				#print temp_poss_grid[i-1]
				# print "i was", i,
				i -= 1
				backtrack = True
				# print "remove 1, i is now", i
			counter += 1
		print temp_grid




		# i = 0
		# temp_grid = grid[:]
		# temp_poss_grid = poss_grid[:]
		# counter = 0
		# backtrack = False

		# while i < 81:# and counter < 20:
		# 	counter += 1
		# 	print i , temp_poss_grid[i]

		# 	#print len(self.poss_grid[i])
		# 	if backtrack == True and len(self.poss_grid[i]) == 1:
		# 		i -=1

		# 	else:
		# 		# print counter

		# 		if len(temp_poss_grid[i]) > 0:
		# 			test_value = min(temp_poss_grid[i])
		# 			if self.check_valid(i, temp_grid, test_value):
		# 				temp_grid[i] = test_value
		# 				temp_poss_grid[i] = [test_value]
		# 				i += 1
		# 			else:
		# 				#print counter
		# 				temp_poss_grid[i].remove(test_value)
		# 		else:
		# 			# print counter
		# 			backtrack = True
		# 			#print temp_poss_grid[i], self.poss_grid[i]
		# 			temp_poss_grid[i] = self.poss_grid[i]

		# 			if len(self.poss_grid[i-1]) > 1:
		# 				temp_poss_grid[i - 1] = [i for i in self.poss_grid[i - 1] if i > temp_grid[i - 1]]
		# 			i -= 1
		# self.grid = temp_grid
		# self.print_grid()





	def check_valid(self, index, grid, value):
		if value in self.poss_index_values(index, grid) or value == self.grid[index]:
			return True
		return False

	# returns set of possible solutions
	def poss_index_values(self, index, grid):
		
		return self.standard_set ^ (self.build_row(index, grid) | self.build_col(index, grid) | self.build_box(index, grid))


	def build_possible(self):
		return [list(self.poss_index_values(i, self.grid)) if self.grid[i] == 0 else [self.grid[i]] for i in range(81)]

	# returns a set of numbers in row when given index
	def build_row(self, index, grid):
		row_num = index // 9
		return set([grid[i + (row_num * 9)] for i in range(9)])

	# returns a set of column in row when given index
	def build_col(self, index, grid):
		col_num = index % 9
		return set([grid[col_num + (9 * i)] for i in range(9)])

	# returns a set of numbers in box when given index
	def build_box(self, index, grid):
		box_col_num = index // 27
		box_row_num = (index % 9) // 3
		return set([grid[(i + (j * 9) + (box_col_num * 27) + (box_row_num * 3))] for i in range(3) for j in range(3)])



			

grid = [8, 0, 0,    4, 0, 6,    0, 0, 7,
		0, 0, 0,    0, 0, 0,    4, 0, 0,
		0, 1, 0,    0, 0, 0,    6, 5, 0,

		5, 0, 9,    0, 3, 0,    7, 8, 0,
		0, 0, 0,    0, 7, 0,    0, 0, 0,
		0, 4, 8,    0, 2, 0,    1, 0, 3,

		0, 5, 2,    0, 0, 0,    0, 9, 0,
		0, 0, 1,    0, 0, 0,    0, 0, 0,
		3, 0, 0,    9, 0, 2,    0, 0, 5]

# grid=[8, 2, 3,    4, 1, 6,    9, 0, 7,
# 		0, 0, 0,    0, 0, 0,    4, 0, 0,
# 		0, 1, 0,    0, 0, 0,    6, 5, 0,

# 		5, 0, 9,    0, 3, 0,    7, 8, 0,
# 		0, 0, 0,    0, 7, 0,    0, 0, 0,
# 		0, 4, 8,    0, 2, 0,    1, 0, 3,

# 		0, 5, 2,    0, 0, 0,    0, 9, 0,
# 		0, 0, 1,    0, 0, 0,    0, 0, 0,
# 		3, 0, 0,    9, 0, 2,    0, 0, 5]

s = Sudoku(grid)
#print s.poss_index_values(2, grid)
#print s.build_possible()
#print s.check_valid(7, grid, 3)
print s.s_solve()