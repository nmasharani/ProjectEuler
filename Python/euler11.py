grid = []
f = open('gridnums.txt','r')

for line in f:
	grid.append(line.strip("\n").split(" "))

f.close()

product = 0

nrows = len(grid)
ncols = len(grid[0])

# left to right
# up to down
# diagonal 1
# diagonal 2

cd 