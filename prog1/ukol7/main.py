def gcd1(a, b):
    if a == 0 or b == 0:
        return a + b
    if a % b == 0:
        return b
    if b % a == 0:
        return a
    if a < 0:
        return gcd1(-a, b)
    if b < 0:
        return gcd1(a, -b)
    return gcd1(a%b, a)
def lcm1(a, b):
    return a * b // gcd1(a, b)

def lcm(*args):
    if len(args) == 1:
        return args[0]
    accum = 1
    for i in args:
        accum = lcm1(accum, i)
    return accum

def gcd(*args):
    if len(args) == 1:
        return args[0]
    accum = gcd1(*args[:2])
    for i in args[2:]:
        accum = gcd1(accum, i)
    return accum

def add_rows(row1, row2):
    return [a + b for a, b in zip(row1, row2)]

def scalar_div(scalar, row):
    return [i // scalar for i in row]

def scalar_mul(scalar, row):
    return [scalar * i for i in row]

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
col, row = 0, 0
num_cols = len(matrix[0])  # Total number of columns in the matrix

while row < n and col < num_cols:
    # Find all nonzero rows in the current column
    nonzero_rows = [i for i in range(row, n) if matrix[i][col] != 0]
    if not nonzero_rows:
        exit(1) # No solution
    if matrix[row][col] == 0:
        nonzero_row = nonzero_rows[0]
        matrix[row], matrix[nonzero_row] = matrix[nonzero_row], matrix[row]
        continue
    goal = lcm(*[matrix[i][col] for i in nonzero_rows])
    matrix[row] = scalar_mul(goal // matrix[row][col], matrix[row])
    for i in nonzero_rows[1:]:  # Skip the pivot row
        factor = -goal // matrix[i][col]
        matrix[i] = add_rows(matrix[i], scalar_mul(factor, matrix[row]))
    for i in nonzero_rows:
        row_gcd = gcd(*matrix[i])
        matrix[i] = scalar_div(row_gcd, matrix[i])
    col += 1
    row += 1

results = [0] * n
for i in reversed(range(n)):
    results[i] = matrix[i][-1]
    for j in range(i + 1, n):
        results[i] -= matrix[i][j] * results[j]
    if matrix[i][i] != 0:
        results[i] /= matrix[i][i]  # Convert to float
    else:
        print("No solution")
        exit(1)
print(*results, sep='\n')
