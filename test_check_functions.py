from check_functions import check_name, check_name_len, check_sid_len

def test_check_name():
    assert check_name("hello") == True
    assert check_name("he llo") == True
    assert check_name("he1ю") == True
    assert check_name("hell ") == False
    assert check_name(" he1ю¡") == False
    assert check_name("⅞+⅛!=ю ") == False

def test_check_name_len():
    assert check_name_len("hellohaha") == True
    assert check_name_len("⅞+⅛!=ю") == True
    assert check_name_len("ю ю") == True
    assert check_name_len("⅞+⅛!=ю!!!!") == True
    assert check_name_len("helюw rld !¡!¡!¡haha") == False  # Should be False if byte count > 20



def test_check_sid_len():
    assert check_sid_len("1155111111") == True
    assert check_sid_len(1155111111) == True
    assert check_sid_len("¹¹55") == False
    assert check_sid_len(" 115511111") == False
    assert check_sid_len(5511111110) == False
    assert check_sid_len("1155 11111") == False

