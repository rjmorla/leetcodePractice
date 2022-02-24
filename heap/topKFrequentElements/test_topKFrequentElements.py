from topKFrequentElements import topKFrequent

def test_1():
    assert topKFrequent([1,1,1,2,2,3], 2) == [1,2] or topKFrequent([1,1,1,2,2,3], 2) == [2,1]