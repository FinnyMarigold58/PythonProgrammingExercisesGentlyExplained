def getChessSquareColor(column, row):
    if (column > 7 or column < 0) and (row > 7 or row < 0):
        return ""
    
    if column % 2 == row % 2:
        return 'white'
    else:
        return 'black'

## Test Statements
assert getChessSquareColor(1, 1) == 'white' 
assert getChessSquareColor(2, 1) == 'black' 
assert getChessSquareColor(1, 2) == 'black' 
assert getChessSquareColor(8, 8) == '' 
assert getChessSquareColor(0, 8) == '' 
assert getChessSquareColor(2, 9) == '' 
