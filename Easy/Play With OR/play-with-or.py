#User function Template for python3

class Solution:
    def game_with_number (self, arr,  n) : 
        #Complete the function
  
        listt =[]
        for i in range(n-1):
            sum = 0
            sum =arr[i] | arr[i+1]
            listt.append(sum)
        listt.append(arr[-1])
        return listt


#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends