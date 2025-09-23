

#m1
def reverse_el(arr):
    K = 0
    for i in range(len(arr)-1,len(arr)//2,-1):
        temp = arr[K]
        arr[K] = arr[i]
        arr[i] = temp
        

        K+=1
    return arr
arr = [12,32,4,5,56,6,3]
print(reverse_el(arr))

#m2
def reverse_el(arr):
    A =  [0]*len(arr)
    K = 0
    for i in range(len(arr)-1,-1,-1):
        A[K] = arr[i]
        K+=1
    for j in range(len(A)):
        arr[j] = A[j]
    return arr 
arr = [12,3,4,4,5,66,7]
print(reverse_el(arr))
