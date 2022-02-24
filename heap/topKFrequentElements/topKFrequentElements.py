import heapq

def topKFrequent(nums, k):
    ans = []
    dict = {}

    for num in nums: 
        if num not in dict: 
            dict[num] = 1
        else: 
            dict[num] += 1

    for key, val in dict.items():
        if len(ans) < k:
            heapq.heappush(ans, [val, key])
        else: 
            heapq.heappushpop(ans, [val, key])

    return [key for value, key in ans]