def bigger_guy(guy,guy2):
    if guy > guy2:
        return guy
    else:
        return guy2



def test_bigger_guy():
    assert bigger_guy(1,2) == 2
    assert bigger_guy(10,20) == 20
    assert bigger_guy(20,10) == 20
    assert bigger_guy(10,10) == 10
    assert bigger_guy(2,1) == 2
    print("Your code is correct ")
test_bigger_guy()
