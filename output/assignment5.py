def max_sum_subarray_k(arr, k):
    n = len(arr)
    
    # Step 1: first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Step 2: slide window
    for i in range(k, n):
        window_sum += arr[i]     
        window_sum -= arr[i-k]    
        
        max_sum = max(max_sum, window_sum)
    
    return max_sum



arr = [2, 1, 5, 1, 3, 2, 7, 1]
k = 3
print(max_sum_subarray_k(arr, k))  