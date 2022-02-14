import heapq
def topKFrequent(nums, k):
    dict, ans = {}, []

    # Make dictionary to keep hash table of value counts in num
    for num in nums: 
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    # Push to heap
    for key, value in dict.items():
        if len(ans) < k:
            heapq.heappush(ans, [-value, key]) # negative value since python default is minheap
        else:
            heapq.heappushpop(ans, [-value, key])

    return (key for value, key in ans) # return only key from value key pairs