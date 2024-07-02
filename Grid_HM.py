 # Grid using hashmap
class Solution:
    def uniquePaths(self, m, n):
        hashmap = {}
        count = 0
        return self.recurse(0, 0, m, n, count, hashmap)    


        
    def recurse(self, i, j, m, n, count, hashmap):
        if i == m or j == n:
            return 0
        if i == m-1 and j == n-1:
            count += 1
            return 1
            
        val = str(i)+ "-" + str(j)
        if val in hashmap:
            return hashmap[val]
        hashmap[str(i)+ "-" +str(j)] = self.recurse(i+1, j, m, n, count, hashmap) + self.recurse(i, j+1, m, n, count, hashmap)
        return hashmap[str(i)+ "-" +str(j)]
                    

                    
