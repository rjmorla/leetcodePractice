from construct2DArray import construct2DArray

def test_1():
    assert construct2DArray([1,2,3,4], 2, 2) == [[1,2],[3,4]]

def test_2():
    assert construct2DArray([1,2,3], 1, 3) == [[1,2,3]]

def test_3():
    assert construct2DArray([1,2], 1, 1) == []
