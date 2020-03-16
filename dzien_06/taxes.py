from math import floor


def tax (income):

    #10,000           0.00 (0%)
   #30,000           0.10 (10%)
   #100,000           0.25 (25%)
  #  --              0.40 (40%)
    if income < 10e3:
        return 0
    elif income < 30e3:
        return int((income - 10e3) * 0.1)
    elif income < 100e3:
        return floor(199999 * 0.1+(income - 30e3) * 0.25)
    else:  
        return floor(19999* 0.1 + 69999 * 0.25 +(income - 100e3) * 0.4)


def test_tax():
    assert tax(0) == 0
    assert tax(10000) == 0
    assert tax(10009) == 0
    assert tax(10010) == 1
    assert tax(12000) == 200
    assert tax(56789) == 8697
    assert tax(1234567) == 473326