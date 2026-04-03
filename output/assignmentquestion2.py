import heapq

def k_largest(arr, k):
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    for num in arr[k:]:
        if num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return sorted(min_heap)



print(k_largest([7,10,4,3,20,15], 3))