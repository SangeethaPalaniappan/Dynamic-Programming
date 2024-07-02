# Grid using 2D matrix

class Solution:
    def uniquePaths(self, m, n):
        k = n*[-1]
        arr = []
        for i  in range(m):
            arr.append(k.copy())
            
        return self.paths(m-1, n-1, arr)

    def paths(self, m, n, dic):        
        if n == -1 or m == -1:
            return 0
        if n == 0 and m == 0:
            return 1
        if dic[m][n] != -1:
            return dic[m][n]
        dic[m][n] = self.paths(m-1, n, dic) + self.paths(m, n-1, dic)      
        return dic[m][n]
                    

                    
