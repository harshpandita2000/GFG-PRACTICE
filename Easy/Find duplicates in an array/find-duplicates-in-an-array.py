class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	duplicates = set()
        seen = set()
        
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        result = sorted(list(duplicates))
        if not result:
            return [-1]
        else:
            return result
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends