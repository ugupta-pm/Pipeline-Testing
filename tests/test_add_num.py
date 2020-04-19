from package.add_num import add

def test_add_num():
    assert add(2,3) == 5
    assert add(3,3) == 6
    assert add(5,6) == 11
    assert add(5,5) == 10