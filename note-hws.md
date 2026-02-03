## Timeline

- 2026.02.02 完成hw01, hw02

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

## Hw02

所谓High-order function，其实就是支持将函数作为其他函数的参数，用来构建更加强大的抽象。

### Q1: Product

```python
def product(n, term):
    """Return the product of the first n terms in a sequence.

    n: a positive integer
    term:  a function that takes one argument to produce the term

    >>> product(3, identity)  # 1 * 2 * 3
    6
    >>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)    # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    >>> product(3, increment) # (1+1) * (2+1) * (3+1)
    24
    >>> product(3, triple)    # 1*3 * 2*3 * 3*3
    162
    """
    "*** YOUR CODE HERE ***"
    result = 1
    for i in range(1, n+1):
        result *= term(i)
    return result
```

### Q2: Accumulate

先实现accumulate，然后利用accumulate可以很快速地实现`summation_using_accumulate`和`product_using_accumulate`。

```python
def accumulate(fuse, start, n, term):
    """Return the result of fusing together the first n terms in a sequence 
    and start.  The terms to be fused are term(1), term(2), ..., term(n). 
    The function fuse is a two-argument commutative & associative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    """
    "*** YOUR CODE HERE ***"
    result = start
    for i in range(1, n+1):
        result = fuse(result, term(i))
    return result


def summation_using_accumulate(n, term):
    """Returns the sum: term(1) + ... + term(n), using accumulate.

    >>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
    55
    >>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
    45
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(add, 0, 5, term)


def product_using_accumulate(n, term):
    """Returns the product: term(1) * ... * term(n), using accumulate.

    >>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
    576
    >>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
    524880
    >>> # This test checks that the body of the function is just a return statement.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
    ['Expr', 'Return']
    """
    return accumulate(mul, 1, n, term)
```

### Q3: Make Repeater

这个函数的实现不难，但是需要一定的递归思维和对高阶函数的理解。

```python
def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return lambda x : f(x)        
    return lambda x : f(make_repeater(f, n-1)(x))
```

该函数要靠递归来实现，base case为n==1，返回一个函数，其接收一个参数x，返回对其调用一次f的结果。

递归的case需要仔细思考一下其中的逻辑：

- 首先要返回的是接收一个参数的函数
- 该函数的作用是对x调用n次函数f
- 那么我们可以递归调用`make_repeater(f, n-1)`来获取重复对x调用n-1次f函数的函数
- 然后将其作用于x，最后在外层再套一个f，就完成任务了

测试一下：

```shell
~/minghan/courses/CS61A/hws/hw02 % python3 ok --score --local
=====================================================================
Assignment: Homework 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Doctests for product

>>> from hw02 import *
>>> product(3, identity)  # 1 * 2 * 3
6
>>> product(5, identity)  # 1 * 2 * 3 * 4 * 5
120
>>> product(3, square)    # 1^2 * 2^2 * 3^2
36
>>> product(5, square)    # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
14400
>>> product(3, increment) # (1+1) * (2+1) * (3+1)
24
>>> product(3, triple)    # 1*3 * 2*3 * 3*3
162
Score: 1.0/1

---------------------------------------------------------------------
Doctests for accumulate

>>> from hw02 import *
>>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
15
>>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
26
>>> accumulate(add, 11, 0, identity) # 11 (fuse is never used)
11
>>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
25
>>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
72
>>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
>>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
19
Score: 1.0/1

---------------------------------------------------------------------
Doctests for summation_using_accumulate

>>> from hw02 import *
>>> summation_using_accumulate(5, square) # square(1) + square(2) + ... + square(4) + square(5)
55
>>> summation_using_accumulate(5, triple) # triple(1) + triple(2) + ... + triple(4) + triple(5)
45
>>> # This test checks that the body of the function is just a return statement.
>>> import inspect, ast
>>> [type(x).__name__ for x in ast.parse(inspect.getsource(summation_using_accumulate)).body[0].body]
['Expr', 'Return']
Score: 1.0/1

---------------------------------------------------------------------
Doctests for product_using_accumulate

>>> from hw02 import *
>>> product_using_accumulate(4, square) # square(1) * square(2) * square(3) * square()
576
>>> product_using_accumulate(6, triple) # triple(1) * triple(2) * ... * triple(5) * triple(6)
524880
>>> # This test checks that the body of the function is just a return statement.
>>> import inspect, ast
>>> [type(x).__name__ for x in ast.parse(inspect.getsource(product_using_accumulate)).body[0].body]
['Expr', 'Return']
Score: 1.0/1

---------------------------------------------------------------------
Doctests for make_repeater

>>> from hw02 import *
>>> add_three = make_repeater(increment, 3)
>>> add_three(5)
8
>>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
243
>>> make_repeater(square, 2)(5) # square(square(5))
625
>>> make_repeater(square, 3)(5) # square(square(square(5)))
390625
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    product: 1.0/1
    accumulate: 1.0/1
    summation_using_accumulate: 1.0/1
    product_using_accumulate: 1.0/1
    make_repeater: 1.0/1

Score:
    Total: 5.0
```

## Hw03

### Q1: Num Eights

```python
def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    if n % 10 == 8:
        return 1 + num_eights(n // 10)
    return num_eights(n // 10)
```

### Q2: Digit Distance

因为要比较n中连续的两个数字的distance，而又无法使用赋值运算，因此需要添加一个helper函数，其接受两个参数来记录前一个数字和n的剩余值。

```python
def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777) # 0 + 0
    0
    >>> digit_distance(314) # 2 + 3
    5
    >>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
    32
    >>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(prev, n):
        if n == 0:
            return 0
        return helper(n % 10, n // 10) + abs(prev - (n % 10))
    return helper(n % 10, n // 10)
```

### Q3: Interleaved Sum

我的第一反应是从n开始不断减治，然后使用求余运算来区分当前的n是奇数还是偶数，然后分别调用`odd_func`和`even_func`，但是题目要求不能使用求余运算，只能另寻出路了。

> **Hint:** Introduce an inner helper function that takes an odd number `k` and computes an interleaved sum from `k` to `n` (including `n`).

根据题目所给提示，可以构建两个辅助函数，一个用于处理奇数，另一个用于处理偶数。

```python
def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
    True
    """
    "*** YOUR CODE HERE ***"
    def odd_helper(k, n):
        if k > n:
            return 0
        return odd_helper(k + 2, n) + odd_func(k)

    def even_helper(k, n):
        if k > n:
            return 0
        return even_helper(k + 2, n) + even_func(k)

    return odd_helper(1, n) + even_helper(2, n)
```

### Q4: Count Dollars

参考`count_partitions`函数的实现：

```python
def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
    		return 1
    elif n < 0:
				return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
```

用类似的思路实现`count_dollars`：

```python
def count_dollars(total):
    """Return the number of ways to make change.

    >>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(total, bill):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif bill == None:
            return 0
        else:
            return helper(total - bill, bill) + helper(total, next_smaller_dollar(bill))
    return helper(total, 100)
```

测试：

```shell
~/minghan/courses/CS61A/hws/hw03 % python3 ok --score --local
=====================================================================
Assignment: Homework 3
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Doctests for num_eights

>>> from hw03 import *
>>> num_eights(3)
0
>>> num_eights(8)
1
>>> num_eights(88888888)
8
>>> num_eights(2638)
1
>>> num_eights(86380)
2
>>> num_eights(12345)
0
>>> num_eights(8782089)
3
>>> from construct_check import check
>>> # ban all assignment statements
>>> check(HW_SOURCE_FILE, 'num_eights',
...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
True
Score: 1.0/1

---------------------------------------------------------------------
Doctests for digit_distance

>>> from hw03 import *
>>> digit_distance(3)
0
>>> digit_distance(777) # 0 + 0
0
>>> digit_distance(314) # 2 + 3
5
>>> digit_distance(31415926535) # 2 + 3 + 3 + 4 + ... + 2
32
>>> digit_distance(3464660003)  # 1 + 2 + 2 + 2 + ... + 3
16
>>> from construct_check import check
>>> # ban all loops
>>> check(HW_SOURCE_FILE, 'digit_distance',
...       ['For', 'While'])
True
Score: 1.0/1

---------------------------------------------------------------------
Doctests for interleaved_sum

>>> from hw03 import *
>>> identity = lambda x: x
>>> square = lambda x: x * x
>>> triple = lambda x: x * 3
>>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
29
>>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
41
>>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
32
>>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
28
>>> from construct_check import check
>>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
True
>>> check(HW_SOURCE_FILE, 'interleaved_sum', ['BitAnd', 'BitOr', 'BitXor']) # ban bitwise operators, don't worry about these if you don't know what they are
True
Score: 1.0/1

---------------------------------------------------------------------
Doctests for count_dollars

>>> from hw03 import *
>>> count_dollars(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
6
>>> count_dollars(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
4
>>> count_dollars(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
10
>>> count_dollars(45)  # How many ways to make change for 45 dollars?
44
>>> count_dollars(100) # How many ways to make change for 100 dollars?
344
>>> count_dollars(200) # How many ways to make change for 200 dollars?
3274
>>> from construct_check import check
>>> # ban iteration
>>> check(HW_SOURCE_FILE, 'count_dollars', ['While', 'For'])
True
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    num_eights: 1.0/1
    digit_distance: 1.0/1
    interleaved_sum: 1.0/1
    count_dollars: 1.0/1

Score:
    Total: 4.0
```

### Q5: Count Dollars Upward

`count_dollars_upward`：

```python
def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100

def count_dollars_upward(total):
    """Return the number of ways to make change using bills.

    >>> count_dollars_upward(15)  # 15 $1 bills, 10 $1 & 1 $5 bills, ... 1 $5 & 1 $10 bills
    6
    >>> count_dollars_upward(10)  # 10 $1 bills, 5 $1 & 1 $5 bills, 2 $5 bills, 10 $1 bills
    4
    >>> count_dollars_upward(20)  # 20 $1 bills, 15 $1 & $5 bills, ... 1 $20 bill
    10
    >>> count_dollars_upward(45)  # How many ways to make change for 45 dollars?
    44
    >>> count_dollars_upward(100) # How many ways to make change for 100 dollars?
    344
    >>> count_dollars_upward(200) # How many ways to make change for 200 dollars?
    3274
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_dollars_upward', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(total, bill):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif bill == None:
            return 0
        else:
            return helper(total - bill, bill) + helper(total, next_larger_dollar(bill))
    return helper(total, 1)
```

### Q6: Towers of Hanoi

```python
def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    def hanoi(n, start, mid, end):
        if n < 1:
            return
        hanoi(n-1, start, end, mid)
        print_move(start, end)
        hanoi(n-1, mid, start, end)

    hanoi(n, start, 2, end)
```

### Q7: Anonymous Factorial

这道题目看起来很复杂，但是理清思路后其实不难。

解决问题的关键就在于弄明白：如何在lambda函数中调用自身？

Python是支持高阶函数的，因此可以利用高阶函数来实现。

```python
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda n: f(f, n))(lambda f, n: 1 if n == 1 else mul(n, f(f, n-1)))
```

