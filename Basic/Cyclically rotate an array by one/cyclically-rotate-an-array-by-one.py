#User function Template for python3

def rotate( arr, n):
    el=arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
        
    arr[0]=el
        
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends