from operator import add, sub

# Q1: A Plus Abs B
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


# Q2: Two of Three
def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    # my solution:
    # calculate all the combinations of m*m+n*n results and use min() to get the smallest one.

    return min(i*i+j*j, j*j+k*k, k*k+i*i)

def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


# Q3: Largest Factor
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    # my solution:
    # 1. use a pointer variable (p) for storing the last factor.
    # 2. add 1 to the initiator variable (i) in each loop until i is equal to n.

    i = 1
    p = None

    while i <= n:

        if i == n:
            return p

        if n % i == 0:
            p = i
        
        i += 1


# Q4: Hailstone
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    # my solution:
    # 1. print n in each loop.
    # 2. do the calculation given by the question.
    # 3. stop the loop when n is equal to 1.
    # 4. count steps start with 1.
    
    count = 1

    while n >= 1:

        print(n)

        if n == 1:
            break
        
        else:
            count += 1

            if n % 2 == 0:
                n //= 2
            elif n != 1:
                n = n * 3 + 1

    return count
