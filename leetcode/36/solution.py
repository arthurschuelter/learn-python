from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = self.isValidRow(board)
        column = self.isValidColumn(board)
        chunk = self.isValidChunks(board)

        return row and column and chunk

    def isValidRow(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidArray(row):
                print(f"❌ Row invalid")
                return False
        print(f"✅ Row valid")
        return True

    def isValidColumn(self, board: List[List[str]]) -> bool:
        for column in zip(*board):
            if not self.isValidArray(column):
                print(f"❌ Column invalid")
                return False
        print(f"✅ Column valid")
        return True
    
    def isValidChunks(self, board: List[List[str]]) -> bool:
        for j in range(0, len(board), 3):
            for z in range(0, 9, 3):
                chunk = []
                for i in range(z, z+3):
                    row = board[i][j:j+3]
                    chunk.extend(row)
                # print(chunk)
                if not self.isValidArray(chunk):
                    print(f"❌ Chunks invalid")
                    return False
        print(f"✅ Chunks valid")
        return True

    def isValidArray(self, arr: List[str]) -> bool:
        counter = Counter([r for r in arr if r != "."])
        for item, freq in counter.items():
            if freq > 1: 
                return False
        return True