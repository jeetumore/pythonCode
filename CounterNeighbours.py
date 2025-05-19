

rows = len(matics)
cols = len(matrics[0])

def countNeighbours(r, c):
    nei = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if ((i == r and j == c) or i < 0 and j < 0 or  or i == rows and j == cols):
                continue
            if board[r][c] in [1, 3]:
                nei += 1
        return nei