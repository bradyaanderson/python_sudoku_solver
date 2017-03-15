def print_grid():
	for row in grid:
		if grid.index(row) % 3 == 0:
			print ""
		print "%s %s %s  %s %s %s  %s %s %s" %  tuple(row[i] for i in range(9))

def check_complete():
	for i in range(9):
		if 0 in grid[i]:
			return False
	return True




def find_possible(x,y):
	poss_values = []
	row_poss = check_row(x,y)
	col_poss = check_col(x,y)
	box_poss = check_box(x,y)

	for value in row_poss:
		if value in col_poss:
			if value in box_poss:
				poss_values.append(value)

	if len(poss_values) == 1:
		return poss_values[0]
	else:
		return 0

def check_row(x,y):
	row_poss = []

	for i in range(1,10):
		if i not in grid[y]:
			row_poss.append(i)

	return row_poss


def check_col(x,y):
	col = []
	col_poss = []

	for i in range(9):
		col.append(grid[i][x])

	for i in range(1,10):
		if i not in col:
			col_poss.append(i)

	return col_poss


def check_box(x,y):
	box = []
	box_poss = []

	box_x = x // 3
	box_y = y // 3

	for i in range(3):
		for j in range(3):
			box.append(grid[(box_y * 3) + i][(box_x * 3) + j])

	for i in range(1,10):
		if i not in box:
			box_poss.append(i)

	return box_poss


#grid = [[0] * 9] * 9
grid = 	[[0, 2, 0,    9, 4, 0,    0, 0, 3],
		 [9, 0, 6,    0, 2, 3,    0, 0, 8],
		 [0, 3, 0,    0, 0, 8,    0, 7, 2],

		 [0, 0, 0,    0, 0, 0,    0, 0, 5],
		 [3, 6, 1,    5, 0, 9,    2, 4, 7],
		 [8, 0, 0,    0, 0, 0,    0, 0, 0],

		 [1, 5, 0,    8, 0, 0,    0, 3, 0],
		 [6, 0, 0,    3, 7, 0,    5, 0, 1],
		 [4, 0, 0,    0, 5, 2,    0, 6, 0]]


poss_grid = [[[]] * 9] * 9
complete = False

while complete == False:

	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				grid[y][x] = find_possible(x,y)

	complete = check_complete()

print_grid()












