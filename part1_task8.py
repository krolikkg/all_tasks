def choice_to_number(choice):
    if choice == "Usain":
        return 1
    elif choice == "Me":
        return 2
    else:
        return 3

def number_to_choice(number):
    if number == 1:
        return "Usain"
    elif number == 2:
        return "Me"
    else:
        return "Aybek"

def test_choice_to_number():
    assert choice_to_number("Usain") == 1
    assert choice_to_number("Me") == 2
    assert choice_to_number("Aybek") == 3

def test_number_to_choice():
    assert number_to_choice(1) == "Usain"
    assert number_to_choice(2) == "Me"
    assert number_to_choice(3) == "Aybek"

def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        print("wrong")
    else:
        print("success")
test_all()
