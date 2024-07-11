# Required Questions

## What Would Python Display? (WWPD)
### Q1: WWPD: Control
> Use Ok to test your knowledge with the following "What Would Python Display?" questions:
> ```bash
> python3 ok -q control -u
> ```

```python
>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
______

>>> xk(10, 6)
______

>>> xk(4, 6)
______

>>> xk(0, 0)
______
```
```python
>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     if x > 0:
...         print('positive')
...     else:
...         print(0)
>>> how_big(7)         # A returned string is displayed with single quotes
______

>>> print(how_big(7))  # A printed string has no quotes
______

>>> how_big(12)
______

>>> print(how_big(12))
______

>>> print(how_big(1), how_big(0))
______
```
```python
>>> n = 3
>>> while n >= 0:
...     n -= 1
...     print(n)
______
```
```python
>>> negative = -12
>>> while negative:  # All numbers are true values except 0
...    if negative + 6:
...        print(negative)
...    negative += 3
______
```

### Q2: Debugging Quiz
The following is a quick quiz on different debugging techniques that will be helpful for you to use in this class. You can refer to the [debugging article](https://cs61a.org/articles/debugging/) to answer the questions.

Use Ok to test your understanding:
```bash
python3 ok -q debugging-quiz -u
```

## Write Code
### Q3: Falling Factorial
Let's write a function `falling`, which is a "falling" factorial that takes two arguments, `n` and `k`, and returns the product of `k` consecutive numbers, starting from `n` and working downwards. When `k` is `0`, the function should return `1`.

```python
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
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:
```bash
python3 ok -q falling
```

### Q4: Divisible By k
Write a function `divisible_by_k` that takes positive integers `n` and `k`. It prints all positive integers less than or equal to `n` that are divisible by `k` from smallest to largest. Then, it returns how many numbers were printed.

```python
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
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:
```bash
python3 ok -q divisible_by_k
```

### Q5: Sum Digits
Write a function that takes in a nonnegative integer and sums its digits. (Using floor division and modulo might be helpful here!)

```python
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
    "*** YOUR CODE HERE ***"
```

Use Ok to test your code:
```bash
python3 ok -q sum_digits
```
