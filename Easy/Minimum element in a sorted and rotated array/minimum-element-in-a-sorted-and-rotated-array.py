#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        mini =arr[0]
        for i in range(len(arr)):
            if arr[i]<mini:
                mini=arr[i]
        return mini
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends