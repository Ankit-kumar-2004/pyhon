import heapq

def findKthLargest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        # Keep only k elements in heap
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]



nums = [3, 2, 1, 5, 6, 4]
k = 2

result = findKthLargest(nums, k)
print("Kth largest element is:", result)