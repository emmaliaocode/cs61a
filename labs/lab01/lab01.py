# Q3: Falling Factorial
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    # my solution:
    # 1. set a variable r to store the result of continued multiplication
    # 2. multiply r with n for k time, n is subtracted by 1 in every loop

    if k == 0:
        return 1

    else:
        r = None

        while k != 0:
            if r is None:
                r = n
            else:
                r *= n

            n -= 1
            k -= 1

        return r


# Q4: Divisible By k
def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    # my solution:
    # 1. set a variable p with 0 as an initial value
    #       and set a variable c with 0 as an initial value
    # 2. the idea is to add k to p until p reaches n
    #       and use c to count how many times we add k
    # 3. print every p and return k

    if n < k:
        return 0

    else:
        c = 0
        p = 0

        while p <= n:

            if p == 0:
                p = k

            print(p)
            p += k
            c += 1

        return c


# Q5: Sum Digits
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    # my solution:
    # 1. set a variable r to store the result of the cumulative addition of digits.
    # 2. the digit is equal to the remainder of y divided by 10.
    # 3. accumulatively sum the remainder to r.

    r = 0

    while y >= 10:

        r += y % 10
        y //= 10

    return y + r


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    # my solution:
    # 1. set a flag variable with an initial value as False,
    #       the flag will be updated to True when the 1st 8 is met.
    # 2. check the number backward, by evaluating the remainder of n divided by 10 is equal to 8.
    #       if the remainder is equal to 8, update the flag to True.
    #       if the flag is True, and the remainder is equal to 8 again, return True.
    # 3. flood divided n by 10 to exclude the number of the current loop.

    flag = False

    while n >= 8 and n > 0:

        if flag:
            if n % 10 == 8:
                return True
            else:
                flag = False
        else:
            if n % 10 == 8:
                flag = True

        n //= 10

    return False
