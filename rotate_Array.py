
# Rotate The Array from given d position and d times

#m1
class Rotate:
    def rotate_array(self,arr,d):
        n = len(arr)
        d = d%n
        for i in range(d):
            A = arr.pop(0)
            arr.append(A)
        return arr
obj = Rotate()
print(obj.rotate_array([23,4,4,5,56,6,7,7,8],4))


#m2

class Rotate:
    def rotate_array(self,arr,d):
        n = len(arr)
        d = d%n
        for i in range(d):
            A = arr.pop(0)
            arr.append(A)
        return arr
arr = []
n = int(input("Enter the sise of araay :"))
for i in range(n+1):
    x = int(input())
    arr.append(x)
    
d = int(input("Enter the position for rotating the array element :"))
obj = Rotate()
print("After rotating the array Element :",obj.rotate_array(arr,d))
