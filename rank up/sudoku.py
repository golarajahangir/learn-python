def valid_solution(board):
    all_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in board:
        if sorted(row) != all_list:
            return False
    for col in range(0, 9):
        if sorted(list(map(lambda row: row[col], board))) != all_list:
            return False
    box = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for row in board[0 + i : 3 + i]:
                for col in range(0 + j, 3 + j):
                    box.append(row[col])
            if sorted(box) == all_list:
                box.clear()
            else:
                return False
    return True


print(
    valid_solution(
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
    )
)
