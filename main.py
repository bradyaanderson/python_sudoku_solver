from copy import deepcopy

class Sudoku():

	def __init__(self, grid):
		self.grid = grid
		self.standard_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
		self.poss_grid = self.build_possible()

	# builds a 2-d list with possible solutions
	def build_possible(self):
		return [list(self.poss_index_values(i, self.grid)) if self.grid[i] == 0 else [self.grid[i]] for i in range(81)]

	# returns set of possible solutions
	def poss_index_values(self, index, grid):
		return self.standard_set ^ (self.build_row(index, grid) | self.build_col(index, grid) | self.build_box(index, grid))

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

	# solves puzzle
	def solve(self):
		# initialize variables
		i = 0
		backtrack = False

		# make copy of lists
		solution_grid = deepcopy(self.grid)
		solution_poss_grid = deepcopy(self.poss_grid)

		# main loop for funciton
		while i < 81:
			
			if len(solution_poss_grid[i]) > 0:
				# lowest value in list becomes test value
				test_value = min(solution_poss_grid[i])

				# checks if value is not solved
				if self.grid[i] != 0:
					solution_grid[i] = self.grid[i]

					# if backtacking, should reset list for index before and decrement
					if (backtrack):
						solution_poss_grid[i - 1] = [j for j in self.poss_grid[i  - 1] if j > solution_grid[i - 1]]
						i -= 1

					# if not backtracking, should increment
					else:
						i += 1

				# if value is valid, place in solution_grid, increment by 1
				elif self.check_valid(i, solution_grid, test_value):
					backtrack = False
					solution_grid[i] = test_value
					i += 1

				# if value is not valid, remove from solution_poss_list, do not increment
				else:
					solution_poss_grid[i].remove(test_value)

			# if there are no values in solution_poss_grid, backtracking starts
			else:
				# reset current grid
				solution_grid[i] = 0
				solution_poss_grid[i] = deepcopy(self.poss_grid[i])

				# modify next grid, if there are more than one value
				if len(solution_poss_grid[i-1]) != 1:
					solution_poss_grid[i - 1] = [j for j in self.poss_grid[i  - 1] if j > solution_grid[i - 1]]

				# decrement index, and set backtacking to true
				i -= 1
				backtrack = True

		return solution_grid

	# returns true or false if value is valid at given index
	def check_valid(self, index, grid, value):
		if value in self.poss_index_values(index, grid) or value == self.grid[index]:
			return True
		return False

	# prints out sudoku board
	def print_grid(self, grid):
		for i in range(81):
			print str(grid[i]),
			# add a black line every 3 columns
			if (i + 1) % 27 == 0 and (i + 1) != 81:
				print '\n'
			# write every column on new line
			elif (i + 1) % 9 == 0:
				print ''
			# seperate every 3 numbers
			elif (i+1) % 3 == 0:
				print ' ',


# -------- MAIN --------

grid =  [0, 7, 4,    0, 5, 0,    3, 2, 0,
		 0, 8, 0,    0, 0, 7,    0, 0, 6,
		 0, 0, 2,    0, 0, 3,    0, 0, 8,

		 0, 0, 0,    4, 7, 6,    0, 0, 3,
		 4, 1, 0,    3, 0, 9,    0, 7, 5,
		 9, 0, 0,    5, 1, 8,    0, 0, 0,

		 7, 0, 0,    9, 0, 0,    4, 0, 0,
		 2, 0, 0,    1, 0, 0,    0, 8, 0,
		 0, 4, 8,    0, 3, 0,    6, 9, 0]

s = Sudoku(grid)

# solve and print in readable format
solution = s.solve()
s.print_grid(solution)