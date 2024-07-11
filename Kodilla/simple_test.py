def example():
    x = 2
    y = 4
    result = x + y
    #return result
    return result

example()

def test_example():
    assert example() == 5 #fail bo nie jest == 6

test_example()