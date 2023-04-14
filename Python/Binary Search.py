def binary_search(arr, x):
    # Set the starting and ending indices for the search
    start = 0
    end = len(arr) - 1
    
    # Loop until the search is complete
    while start <= end:
        # Find the middle index of the search range
        mid = (start + end) // 2
        
        # If the middle element is the target, return its index
        if arr[mid] == x:
            return mid
        
        # If the middle element is less than the target, search the right half
        elif arr[mid] < x:
            start = mid + 1
        
        # If the middle element is greater than the target, search the left half
        else:
            end = mid - 1
            
    # If the target is not in the array, return -1
    return -1

