def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs:
        result += _

    return result









'''
>>> 64 * 78
4992


if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''
