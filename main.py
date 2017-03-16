def print_grid():
	for row in grid:
		if grid.index(row) % 3 == 0:
			print
		print "%s %s %s  %s %s %s  %s %s %s" % tuple(row[i] for i in range(9))


def check_complete():
	if len([i for i in range(9) if 0 in grid[i]]) != 0:
		return False
	return True

def make_col(x):
	return [grid[i][x] for i in range(9)]

def make_box(x,y):
	box_x = x // 3
	box_y = y // 3
	return [grid[(box_y * 3) + i][(box_x * 3) + j] for j in range(3) for i in range(3)]


def find_possible(x,y):
	row_poss = check_row(y)
	col_poss = check_col(x,y)
	box_poss = check_box(x,y)

	poss_values = (row_poss & col_poss & box_poss)
	if len(poss_values) == 1:
		grid_poss[y][x] = []
		return poss_values.pop()

	grid_poss[y][x] = list(poss_values)
	return 0


def check_row(y):
	return set([i for i in range(1,10) if i not in grid[y]])


def check_col(x,y):
	col = make_col(x)
	return set([i for i in range(1,10) if i not in col])


def check_box(x,y):
	box = make_box(x,y)
	return set([i for i in range(1,10) if i not in box])


def find_unique():
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				unique_row(x,y)
				unique_col(x,y)
				unique_box(x,y)

def unique_row(x,y):
	current_set = set(grid_poss[y][x])
	other_set = set()


	# build row set
	for i in range(9):
		if i != x:
			for num in grid_poss[y][i]:
				other_set.add(num)



	poss_set = (current_set - other_set)
	if len(poss_set) == 1:
		grid[y][x] = poss_set.pop()
		grid_poss[y][x] = []

def unique_col(x,y):
	current_set = set(grid_poss[y][x])
	other_set = set()


	# build col set, x is constant, y is changing
##############################################
	for i in range(9):
		if i != y:
			for num in grid_poss[i][x]:
				other_set.add(num)
##############################################


	poss_set = (current_set - other_set)
	if len(poss_set) == 1:
		grid[y][x] = poss_set.pop()
		grid_poss[y][x] = []
	


def unique_box(x,y):
	current_set = set(grid_poss[y][x])
	other_set = set()


	# build box set
##############################################
	box_x = x // 3
	box_y = y // 3

	box_lists = [grid_poss[(box_y * 3) + i][(box_x * 3) + j] for j in range(3) for i in range(3)]
	other_set = set([i for num_list in box_lists for i in num_list])
##############################################


	poss_set = (current_set - other_set)
	if len(poss_set) == 1:
		grid[y][x] = poss_set.pop()
		grid_poss[y][x] = []

grid = 	[[8, 0, 0,    4, 0, 6,    0, 0, 7],
		 [0, 0, 0,    0, 0, 0,    4, 0, 0],
		 [0, 1, 0,    0, 0, 0,    6, 5, 0],

		 [5, 0, 9,    0, 3, 0,    7, 8, 0],
		 [0, 0, 0,    0, 7, 0,    0, 0, 0],
		 [0, 4, 8,    0, 2, 0,    1, 0, 3],

		 [0, 5, 2,    0, 0, 0,    0, 9, 0],
		 [0, 0, 1,    0, 0, 0,    0, 0, 0],
		 [3, 0, 0,    9, 0, 2,    0, 0, 5]]

grid_poss = a =[[[] for j in range(9)] for i in range (9)]

complete = False

while not complete:

	update = False
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				grid[y][x] = find_possible(x,y)
				if grid[y][x] != 0:
					update = True
	if not update:
		find_unique()
		



	complete = check_complete()

print_grid()













