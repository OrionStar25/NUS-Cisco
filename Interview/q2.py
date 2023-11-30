# word1 = "horse"
# word2 = "ros"

word1 = "intention"
word2 = "execution"

initial = [c for c in word1]
target = [c for c in word2]

n = len(initial)
m = len(target)

insertion = 1
deletion = 1
substitution = 1

matrix = []

for i in range(m+1):
    if i == 0:
        row = [j for j in range(n+1)]
    else:
        row = [0 for _ in range(n+1)]
        row[0] = i

    matrix.append(row)

print(matrix)

for i in range(1, m+1):
    for j in range(1, n+1):
        matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
        if target[i-1] != initial[j-1]:
            matrix[i][j] += 1

print(matrix[m][n])

