import math

MAX = 1001

spiral = [[0 for col in range(MAX)] for row in range(MAX)]

row = (MAX/2)
col = (MAX/2)
i = 1
inRow = [0, 1]
inCol = [1, 0]
N = 1
N_IN = 2 * N
inc = 1

spiral[row][col]=i
#i += 1
while i <= pow(MAX,2):
	for x in range(len(inRow)):
		if i >= pow(MAX,2):
			break
		else:
			i += 1
			row = row + int(inRow[x])
			col = col + int(inCol[x])
			spiral[row][col] = i
	if inc == -1:
		inc = 1
	else:
		inc = -1

	N += 1
	inRow = [0 for m in range(N)]
	inCol = [inc for m in range(N)]

	k = 1
	while k <= N:
		inRow.append(inc)
		inCol.append(0)
		k += 1
	if i >= pow(MAX,2):
		break


diag = []

for i in range(len(spiral)):
	if i != (MAX/2):
		diag.append(spiral[i][i])
		diag.append(spiral[i][len(spiral)-1-i])
	else:
		diag.append(spiral[i][i])

print(sum(diag))

