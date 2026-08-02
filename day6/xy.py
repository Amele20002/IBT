#def factorial(n):
   # if n==0:
  #      return 1
   # if n==1:
   #     return 1
    #else:
    #    return n*factorial(n-1)
#print(factorial(4))
def palindrome(arr,target):
    left,right=0,len(arr)-1
    while left<right:
        if arr[left]!=arr[right]:
            return("not a palindrome")
            right-=1
            left+=1
            return("palindrome ")
            x=arr[left,right]
    else:
        print("not a palindrome")
palindrome(arr="sas",target="none")
##merged sort 


