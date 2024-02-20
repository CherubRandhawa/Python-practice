def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        if rows != 9 or cols != 9:
            return False
        for r in range(0,9):      ###for rows
            my_dict = set()  #because set does not store duplicate values 
            for c in range(0,9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] not in my_dict and 1 <= int(board[r][c]) <= 9 :
                    my_dict.add(board[r][c])
                else: 
                    return False
        
        for c in range(0,9):      ### for cols
            my_dict = set()
            for r in range(0,9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] not in my_dict and 1 <= int(board[r][c]) <= 9 :
                    my_dict.add(board[r][c])
                else:
                    return False
        
        for i in range(0,9,3):    ## for 3*3 boxes 
            for j in range(0,9,3):
                my_dict = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] not in my_dict and 1 <= int(board[r][c]) <= 9:
                            my_dict.add(board[r][c])
                        else:
                            return False

        return True

