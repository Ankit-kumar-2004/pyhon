def prefix_sum_queries(arr, queries):
    n = len(arr)
    
    
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    
    result = []
    
    
    for L, R in queries:
        if L == 0:
            result.append(prefix[R])
        else:
            result.append(prefix[R] - prefix[L-1])
    
    return result


arr = [2,4,1,6,3]
queries = [(1,3),(0,4),(2,4)]

print(prefix_sum_queries(arr, queries))