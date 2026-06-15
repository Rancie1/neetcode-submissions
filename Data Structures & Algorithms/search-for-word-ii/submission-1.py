class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res,visit = set(),set()

        def dfs(row, col, word, node):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or (row,col) in visit or board[row][col] not in node.children):
                return
            visit.add((row,col))
            word += board[row][col]
            node = node.children[board[row][col]]
            if node.isWord:
                res.add(word)

            dfs(row+1,col,word,node)
            dfs(row,col+1,word,node)
            dfs(row-1,col,word,node)
            dfs(row,col-1,word,node)

            visit.remove((row,col))


        for row in range(ROWS):
            for col in range(COLS):
                dfs(row,col,"",root)

        return list(res)

            

        
        