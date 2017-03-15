def print_grid():
	for row in grid:
		if grid.index(row) % 3 == 0:
			print
		print "%s %s %s  %s %s %s  %s %s %s" % tuple(row[i] for i in range(9))


def check_complete():
	if len([i for i in range(9) if 0 in grid[i]]) != 0:
		return False
	return True


def find_possible(x,y):
	row_poss = check_row(y)
	col_poss = check_col(x,y)
	box_poss = check_box(x,y)

	poss_values = (row_poss & col_poss & box_poss)
	if len(poss_values) == 1:
		return poss_values.pop()
	return 0


def check_row(y):
	return set([i for i in range(1,10) if i not in grid[y]])


def check_col(x,y):
	col = [grid[i][x] for i in range(9)]
	return set([i for i in range(1,10) if i not in col])


def check_box(x,y):
	box_x = x // 3
	box_y = y // 3

	box = [grid[(box_y * 3) + i][(box_x * 3) + j] for j in range(3) for i in range(3)]
	return set([i for i in range(1,10) if i not in box])


grid = 	[[0, 0, 0,    0, 0, 9,    0, 4, 7],
		 [0, 9, 8,    7, 0, 6,    0, 1, 3],
		 [0, 7, 0,    0, 0, 0,    0, 8, 0],

		 [8, 0, 7,    0, 5, 1,    0, 0, 4],
		 [5, 0, 0,    0, 6, 0,    0, 0, 8],
		 [9, 0, 0,    8, 7, 0,    2, 0, 1],

		 [0, 4, 0,    0, 0, 0,    0, 2, 0],
		 [1, 5, 0,    2, 0, 7,    8, 3, 0],
		 [6, 8, 0,    1, 0, 0,    0, 0, 0]]

complete = False

while not complete:

	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				grid[y][x] = find_possible(x,y)

	complete = check_complete()

print_grid()












