## Timeline

- 2026.02.02 lab00, lab01
- 

## Lab00

### First Assignment

CS61A提供了ok程序来对作业进行自动化评判，可以使用python3运行它（非UCB学生记得添加 `--local` ）。

1) What Would Python Do? (WWPD)

```shell
~/minghan/courses/CS61A/labs/lab00 % python3 ok --local -q  python-basics -u
=====================================================================
Assignment: Lab 0
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Python Basics > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = 20
>>> x + 2
? 22
-- OK! --

>>> x
? 20
-- OK! --

>>> y = 5
>>> y = y + 3
>>> y * 2
? 16
-- OK! --

>>> y + x
? 28
-- OK! --

---------------------------------------------------------------------
OK! All cases for Python Basics unlocked.
```

2) Implementing Functions

实现lab00.py中的`twenty_twenty_four()`函数：

```python
def twenty_twenty_four():
    """Come up with the most creative expression that evaluates to 2024
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_four()
    2024
    """
    return 1012 + 1012
```

3) Running Tests

```shell
~/minghan/courses/CS61A/labs/lab00 % python3 ok --local
=====================================================================
Assignment: Lab 0
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    2 test cases passed! No cases failed.
```

## Lab01

### Q1: Return and Print

```shell
~/minghan/courses/CS61A/labs/lab01 % python3 ok -q return-and-print -u --local
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
return-and-print > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def welcome():
...     print('Go')
...     return 'hello'
>>> def cal():
...     print('Bears')
...     return 'world'
>>> welcome()
(line 1)? Go
(line 2)? 'hello'
-- OK! --

>>> print(welcome(), cal())
(line 1)? Go
(line 2)? Bears
(line 3)? hello world
-- OK! --

---------------------------------------------------------------------
OK! All cases for return-and-print unlocked.
```

注意print中的连续多个参数的输出使用空格隔开。

### Q2: Debugging Quiz

```shell
~/minghan/courses/CS61A/labs/lab01 % python3 ok -q debugging-quiz -u --local
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 1
(cases remaining: 7)

Q: In the following traceback, what is the most recent function call?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) g(x + x, x)
1) f("hi")
2) h(x + y * 5)
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 2
(cases remaining: 6)

Q: In the following traceback, what is the cause of this error?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) the code looped infinitely
1) there was a missing return statement
2) the code attempted to add a string to an integer
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 3
(cases remaining: 5)

Q: How do you write a doctest asserting that square(2) == 4?
Choose the number of the correct choice:
0) def square(x):
       '''
       square(2)
       4
       '''
       return x * x
1) def square(x):
       '''
       doctest: (2, 4)
       '''
       return x * x
2) def square(x):
       '''
       input: 2
       output: 4
       '''
       return x * x
3) def square(x):
       '''
       >>> square(2)
       4
       '''
       return x * x
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 4
(cases remaining: 4)

Q: When should you use print statements?
Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) To ensure that certain conditions are true at certain points in your code
2) For permanant debugging so you can have long term confidence in your code
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 5
(cases remaining: 3)

Q: How do you prevent the ok autograder from interpreting print statements as output?
Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with 'DEBUG:' at the front of the outputted line
2) Print with # at the front of the outputted line
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 6
(cases remaining: 2)

Q: What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits -i
1) python3 -i lab01.py
2) python3 ok -q sum_digits --trace
3) python3 ok -q sum_digits
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 7
(cases remaining: 1)

Q: Which of the following is NOT true?
Choose the number of the correct choice:
0) Testing is very important to ensure robust code
1) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
2) It is generally good practice to release code with assertion statements left in
3) Debugging is not a substitute for testing
4) It is generally bad practice to release code with debugging print statements left in
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for debugging-quiz unlocked.
```

### Q3: Pick a Digit

```python
def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return n // (10 ** k) % 10
```

### Q4: Middle Number

```python
def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return max(min(a, b), min(a, c), min(b, c))
```

测试一下：

```shell
~/minghan/courses/CS61A/labs/lab01 % python3 ok --score --local
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
return-and-print
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
debugging-quiz
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Doctests for digit

>>> from lab01 import *
>>> digit(3579, 2)
5
>>> digit(3579, 0)
9
>>> digit(3579, 10)
0
Score: 1.0/1

---------------------------------------------------------------------
Doctests for middle

>>> from lab01 import *
>>> middle(3, 5, 4)
4
>>> middle(30, 5, 4)
5
>>> middle(3, 5, 40)
5
>>> middle(3, 5, 40)
5
>>> middle(30, 5, 40)
30
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    return-and-print: 0.0/0
    debugging-quiz: 0.0/0
    digit: 1.0/1
    middle: 1.0/1

Score:
    Total: 2.0
```

### Optional Question

Falling Factorial：

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
    if k == 0:
        return 1
    resuslt = 1
    while k > 0:
        resuslt *= n
        n -= 1
        k -= 1
    return resuslt
```

Divisible By k：

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
    count = 0
    for i in range(1, n+1):
        if i % k == 0:
            print(i)
            count += 1
    return count
```

Sum Digits：

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
    sum = 0
    while y > 0:
        sum += y % 10
        y //= 10
    return sum
```

WWPD: What If?

```shell
~/minghan/courses/CS61A/labs/lab01 % python3 ok -q if-statements -u --local
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What If? > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
(line 1)? 10
(line 2)? foo
-- OK! --

---------------------------------------------------------------------
What If? > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def bake(cake, make):
...    if cake == 0:
...        cake = cake + 1
...        print(cake)
...    if cake == 1:
...        print(make)
...    else:
...        return cake
...    return make
>>> bake(0, 29)
(line 1)? 1
(line 2)? 29
(line 3)? 29
-- OK! --

>>> bake(1, "mashed potatoes")
(line 1)? mashed potatoes
(line 2)? "mashed potatoes"
-- OK! --

---------------------------------------------------------------------
OK! All cases for What If? unlocked.
```

Double Eights：

```python
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
    "*** YOUR CODE HERE ***"
    prev = 0
    while n > 0:
        curr = n % 10
        n //= 10
        if curr == 8 and prev == curr:
            return True
        prev = curr
    return False
```

