#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
            m=min(arr)
        
            a=""
            for i in range(0,len(m)):
                for j in range(0,n):
                    if m[i]!=arr[j][i]:
                        if a == "":
                            return -1
                        else:
                            return a
                a+=arr[0][i]
            return a
                 
         
         
         
         


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends