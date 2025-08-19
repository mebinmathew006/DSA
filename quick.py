def quick_sort(arr):
    if len(arr)<=1:
        return arr
        
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x['age'] < pivot['age']]
    right = [x for x in arr if x['age'] > pivot['age']]
    middle =[x for x in arr if x['age'] == pivot['age']]
    return quick_sort(left)+middle+quick_sort(right)
    
   
arr =[{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

print(quick_sort(arr))

 
    
