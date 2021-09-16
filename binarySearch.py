import time
def bS(arr, target, lower, upper):
    if lower+1 >= upper:
        return lower
    middle = (lower + upper)//2
    if arr[middle] <=  target:
        return bS(arr, target, middle, upper)
    return bS(arr, target, lower, middle)



start = time.time()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = bS(arr, 3, 0, 9)
end = time.time()-start
print(num)
print(end)

