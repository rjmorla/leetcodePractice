import heapq
def getLargestElement(nums, k):
    if not nums:
        return None

    maxHeap, res = [], None

    # python is minheap default hence inserting negative num into maxHeap
    for num in nums: 
        heapq.heappush(maxHeap, -num)

    # Make sure to add - sign to get original values while popping
    for _ in range(k):
        res = -heapq.heappop(maxHeap)

    return res