from lesson import division,add_one,add,is_palindrom
import pytest 

# def test_answer():
#     assert add_one(3) == 4
#     assert add_one(8) == 5

# def test_division():
#     assert division(5,2) == 2.5 ,'loops'
#     # assert division(10,0) == 5, 'oops'

# def test_division2():
#     with pytest.raises(ZeroDivisionError):
#         division(3,0) 

# def test_add():
#     test_case = [[1,1,2],[1,2,3],[3,4,7]]
#     for i in test_case:
#         assert add(i[0],i[1]==i[2])

def test_palindrom_function():
    test_case = [('hello', False), ('ondo', False) , ('mom', True),('dad',False)]
    for i in test_case:
        assert is_palindrom(i[0]) == (i[1])












































