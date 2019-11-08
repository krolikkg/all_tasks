def square_number(num):
    if num ** 2:
        return True
    else:
        return False
def test_square_number():
    assert square_number(2) ==4
    assert square_number(8) ==64
    assert square_number(10) ==100
    print("Your code is correct ")
