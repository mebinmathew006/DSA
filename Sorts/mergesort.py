def merge(left,right):
    left_pointer=right_pointer=0
    result = []
    while left_pointer <len(left) and right_pointer < len(right):
        if left[left_pointer]<right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer+=1
        else:
            result.append(right[right_pointer])
            right_pointer+=1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
        
    return result
    
def sort(arr):
    if len(arr)<=1:
        return arr
        
    mid = len(arr)//2
    
    left = sort(arr[:mid])
    
    right =sort(arr[mid:])
    
    return merge(left,right)
    
arr=[54,5,84654,845,4845,84,58,8,4,8,8748,48148,748,8748,74874,8]
print(sort(arr))
