def quick(arr):
    if len(arr)<=1:
        return arr
        
    pivot = arr[0]
    
    left = [x for x in arr[1:] if x < pivot]
    right= [x for x in arr[1:] if x >= pivot]
    
    return quick(left)+[pivot]+quick(right)
    
arr=[55,56,56,9812,16452,5465,454,4,8,84,58454,884,584,45,484,756]

sorted =quick(arr)
print(sorted)
