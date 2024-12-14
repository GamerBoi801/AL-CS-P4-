
def compound_int(money, rate, years):
    if years == 0:
        total = money
    else:
        total = compound_int(money * rate, rate, years - 1)
    return total