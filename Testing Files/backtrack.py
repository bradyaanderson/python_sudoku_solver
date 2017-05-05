# future backtrack version of solver

class Sudoku():

	def __init__(self, grid):
		self.grid = grid

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
			

grid = [8, 0, 0,    4, 0, 6,    0, 0, 7,
		0, 0, 0,    0, 0, 0,    4, 0, 0,
		0, 1, 0,    0, 0, 0,    6, 5, 0,

		5, 0, 9,    0, 3, 0,    7, 8, 0,
		0, 0, 0,    0, 7, 0,    0, 0, 0,
		0, 4, 8,    0, 2, 0,    1, 0, 3,

		0, 5, 2,    0, 0, 0,    0, 9, 0,
		0, 0, 1,    0, 0, 0,    0, 0, 0,
		3, 0, 0,    9, 0, 2,    0, 0, 5]

s = Sudoku(grid)
s.print_grid()