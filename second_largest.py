
# Find The Second largest element
def value(arr):
    A = 0
    B = 0
    for i in range(len(arr)):
        if arr[i] >A:
            B = A
            A = arr[i]
        elif arr[i] > B and arr[i] !=A:
            B = arr[i]
    return B   
arr = [-12332,-266,35,4,5,4,5,4,-26]
print(value(arr))
