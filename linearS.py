import time
arr2 = []

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            arr2.append(i)
        if i == len(arr)-1:
            return arr2



arr = [1, 2, 3, 4, 3, 4, 5, 4, 3]
t = time.time()
print(search(arr, 3))
end = time.time()

print(end - t)



