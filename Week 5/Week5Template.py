def doomsday(y):
    
    """
    >>> doomsday(2012)
    3
    >>> doomsday(1899)
    2
    >>> doomsday(1923)
    3
    >>> doomsday(10000)
    -1
    >>> doomsday(1756)
    -1
    >>> type(doomsday(2010))
    <class 'int'>
    """

    if 1800 < y < 1900:

        x=5
        w = y % 100
        a = w // 12
        b = w % 12
        c = b // 4
        d = (a + b + c) % 7
        e = x + d
        if e > 6:
            e -= 7

        return e

    elif 1900 < y < 2000:

        x=3
        w = y % 100
        a = w // 12
        b = w % 12
        c = b // 4
        d = (a + b + c) % 7
        e = x + d
        if e > 6:
            e -= 7

        return e

    elif 2000 < y < 2100:

        x=2
        w = y % 100
        a = w // 12
        b = w % 12
        c = b // 4
        d = (a + b + c) % 7
        e = x + d
        if e > 6:
            e -= 7 

        return e

    elif 2100 < y < 2200:

        x=0
        w = y % 100
        a = w // 12
        b = w % 12
        c = b // 4
        d = (a + b + c) % 7
        e = x + d
        if e > 6:
            e -= 7 

        return e

    else:
        e = -1

        return e

