import numpy as np
n, m = input().split()
n, m = int(n), int(m)
k = int(input())
board = np.zeros((n, m))
for i in range(k):
    x, y = input().split()
    x, y = int(x), int(y)
    board[x-1, y-1] = 1


def boomb(i, j):
    if i == 0 and j == 0:
        return board[i+1, j] + board[i, j+1]+board[i+1, j+1]
    if i == n-1 and j == m-1:
        return board[i-1, j] + board[i, j-1] + board[i-1, j-1]
    if i == 0 and j == m-1:
        return board[i, j-1] + board[i+1, j] + board[i+1, j-1]
    if i == n-1 and j == 0:
        return board[i-1, j] + board[i, j+1] + board[i-1, j+1]
    if i == 0:
        return board[i, j-1] + board[i, j+1] + board[i+1, j]+board[i+1, j+1]+board[i+1, j-1]
    if j == 0:
        return board[i-1, j] + board[i, j+1] + board[i+1, j]+board[i+1, j+1]+board[i-1, j+1]
    if i == n-1:
        return board[i, j-1] + board[i, j+1] + board[i-1, j]+board[i-1, j+1]+board[i-1, j-1]
    if j == m-1:
        return board[i-1, j] + board[i, j-1] + board[i+1, j]+board[i+1, j-1]+board[i-1, j-1]
    return board[i-1, j] + board[i, j-1] + board[i, j+1] + board[i+1, j]+board[i+1, j+1]+board[i+1, j-1]+board[i-1, j+1]+board[i-1, j-1]


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            print('*', end=" ")
        else:
            print(int(boomb(i, j)), end=" ")
    print()
