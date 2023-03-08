class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ypos = [0] * n
        xChk = [False] * n
        diag1Chk = [False] * (2 * n - 1)
        diag2Chk = [False] * (2 * n - 1)
        
        def dfs(y):
            for x in range(n):
                if not xChk[x] and not diag1Chk[y + x] and not diag2Chk[n-y+x-1]:
                    ypos[y] = x
                    if y == n - 1:
                        tmp = []
                        for j in range(n):
                            s = "." * n
                            i = ypos[j]
                            s = s[:i]+'Q'+s[i+1:]
                            tmp.append(s)
                        self.ans.append(tmp)
                    else:
                        xChk[x] = diag1Chk[y+x] = diag2Chk[n-y+x-1] = True
                        dfs(y+1)
                        xChk[x] = diag1Chk[y+x] = diag2Chk[n-y+x-1] = False
                            
        self.ans = []
        dfs(0)
        return self.ans