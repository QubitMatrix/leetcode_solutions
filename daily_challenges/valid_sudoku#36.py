class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            row=[i for i in x if(i!='.')]
            if(len(set(row))!=len(row)):
                return False
        for x in range(9):
            col=[i[x] for i in board if(i[x]!='.')]
            if(len(set(col))!=len(col)):
                return False
        for countr in range(0,9,3):
            for countc in range(0,9,3):
                mat=[board[rown][coln] for rown in range(countr,countr+3) for coln in range(countc,countc+3) if(board[rown][coln]!='.')]
                if(len(set(mat))!=len(mat)):
                    return False
        return True
