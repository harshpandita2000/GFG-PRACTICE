#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		if len(arr) < 2:
            return -1
		largest = max(arr)
		sec_largest = min(arr)
    		
        for x in arr:
            if x != largest:
                sec_largest = max(sec_largest, x)
    
        if sec_largest == largest:
            return -1
    
        return sec_largest
		
		      
		    

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends