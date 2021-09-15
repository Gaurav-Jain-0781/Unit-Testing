def divide(divident, divisor):
    if divisor == 0:
        raise ValueError("divisor cannot be zero")
    return divident/divisor


def multiply(*args):
    if len(args) == 0:
        raise ValueError("atleast one value is required to do multiplication .")

    value = 1
    for a in args:
        value = value * a
    return value
