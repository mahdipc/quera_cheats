board = [input().strip() for _ in range(7)]

moves = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for r in range(7):
    for c in range(7):
        if board[r][c] != "o":
            continue
        for dr, dc in directions:
            r1, c1 = r + dr, c + dc
            r2, c2 = r + 2 * dr, c + 2 * dc
            if 0 <= r1 < 7 and 0 <= c1 < 7 and 0 <= r2 < 7 and 0 <= c2 < 7:
                if board[r1][c1] == "o" and board[r2][c2] == ".":
                    moves += 1
print(moves)