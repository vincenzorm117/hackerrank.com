

def diagonalDifference(a):
    N = len(a)
    sum = 0
    for i in range(N):
        sum += (a[i][i] - a[i][N-1-i])
    return sum


t = [[11,2,4]]
