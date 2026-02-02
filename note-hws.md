## Timeline

- 2022.02.02 hw01

## Hw01

### Q1: A Plus Abs B

```python
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
```

测试：

```shell
~/minghan/courses/CS61A/hws/hw01 % python3 ok -q a_plus_abs_b --local
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.
```

### Q2: Two of Three

```python
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
    square_i = i * i
    square_j = j * j
    square_k = k * k
    return min(square_i + square_j, square_i + square_k, square_j + square_k)
```

测试：

```shell
~/minghan/courses/CS61A/hws/hw01 % python3 ok -q two_of_three --local
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.
```

### Q3: Largest Factor

```python
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    if n % 2 == 0:
        return n // 2
    
    i = n-1
    while i > 0:
        if n % i == 0:
            return int(i)
        i -= 1
```

测试：

```shell
~/minghan/courses/CS61A/hws/hw01 % python3 ok -q largest_factor --local
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.
```

### Q4: Hailstone

```python
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
    "*** YOUR CODE HERE ***"
    count = 1
    while n > 1:
        count += 1
        print(n)
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2
        
    print(1)
    return count
```

测试：

```shell
~/minghan/courses/CS61A/hws/hw01 % python3 ok -q hailstone --local
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.
```

评分：

```shell
~/minghan/courses/CS61A/hws/hw01 % python3 ok --score --local
=====================================================================
Assignment: Homework 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Doctests for a_plus_abs_b

>>> from hw01 import *
>>> a_plus_abs_b(2, 3)
5
>>> a_plus_abs_b(2, -3)
5
>>> a_plus_abs_b(-1, 4)
3
>>> a_plus_abs_b(-1, -4)
3
Score: 1.0/1

---------------------------------------------------------------------
Doctests for a_plus_abs_b_syntax_check

>>> from hw01 import *
>>> # You aren't expected to understand the code of this test.
>>> import inspect, re
>>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
['return f(a, b)']
Score: 1.0/1

---------------------------------------------------------------------
Doctests for two_of_three

>>> from hw01 import *
>>> two_of_three(1, 2, 3)
5
>>> two_of_three(5, 3, 1)
10
>>> two_of_three(10, 2, 8)
68
>>> two_of_three(5, 5, 5)
50
Score: 1.0/1

---------------------------------------------------------------------
Doctests for two_of_three_syntax_check

>>> from hw01 import *
>>> # You aren't expected to understand the code of this test.
>>> import inspect, ast
>>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
['Expr', 'Assign', 'Assign', 'Return']

# Error: expected
#     ['Expr', 'Return']
# but got
#     ['Expr', 'Assign', 'Assign', 'Return']
Score: 0.0/1

---------------------------------------------------------------------
Doctests for largest_factor

>>> from hw01 import *
>>> largest_factor(15) # factors are 1, 3, 5
5
>>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
40
>>> largest_factor(13) # factor is 1 since 13 is prime
1
Score: 1.0/1

---------------------------------------------------------------------
Doctests for hailstone

>>> from hw01 import *
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
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    a_plus_abs_b: 1.0/1
    a_plus_abs_b_syntax_check: 1.0/1
    two_of_three: 1.0/1
    two_of_three_syntax_check: 0.0/1
    largest_factor: 1.0/1
    hailstone: 1.0/1

Score:
    Total: 5.0
```

### Hw02

