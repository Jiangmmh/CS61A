## Timeline

- 完成2026.02.02 lab00, lab01, lab02
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

## Lab02

### Q1: WWPD: The Truth Will Prevail

具体输入不小心clear了，这个比较简单，我想不太需要参考吧。

```shell
~/minghan/courses/CS61A/labs/lab02 % python3 ok -q short-circuit -u --local
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
The Truth Will Prevail > Suite 1 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
The Truth Will Prevail > Suite 2 > Case 1
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
The Truth Will Prevail > Suite 2 > Case 2
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
The Truth Will Prevail > Suite 3 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for The Truth Will Prevail unlocked.
```

### Q2: WWPD: Higher-Order Functions

```shell
~/minghan/courses/CS61A/labs/lab02 % python3 ok -q hof-wwpd -u --local
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Higher Order Functions > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
? beets
-- OK! --

>>> chocolate
? Function
-- OK! --

>>> chocolate()
(line 1)? sweets
(line 2)? 'cake'
-- OK! --

>>> more_chocolate, more_cake = chocolate(), cake
? sweets
-- OK! --

>>> more_chocolate
? 'cake'
-- OK! --

>>> # Reminder: cake, more_cake, and chocolate were defined/assigned in the code above! 
>>> # It might be helpful to refer to their definitions on the assignment website so you don't have to scroll as much!
>>> def snake(x, y):
...    if cake == more_cake:
...        return chocolate
...    else:
...        return x + y
>>> snake(10, 20)
? Function
-- OK! --

>>> snake(10, 20)()
(line 1)? sweets
(line 2)? 'cake'
-- OK! --

>>> cake = 'cake'
>>> snake(10, 20)
? 30
-- OK! --

---------------------------------------------------------------------
OK! All cases for Higher Order Functions unlocked.
```

### Q3: WWPD: Lambda

```shell
~/minghan/courses/CS61A/labs/lab02 % python3 ok -q lambda -u --local
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 1
(cases remaining: 5)

Q: Which of the following statements describes a difference between a def statement and a lambda expression?
Choose the number of the correct choice:
0) A lambda expression does not automatically bind the function that it returns to a name.
1) A lambda expression cannot return another function.
2) A lambda expression cannot have more than two parameters.
3) A def statement can only have one line in its body.
? 0
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 2
(cases remaining: 4)

Q: How many formal parameters does the following lambda expression have?
lambda a, b: c + d
Choose the number of the correct choice:
0) one
1) three
2) Not enough information
3) two
? 3
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 1 > Case 3
(cases remaining: 3)

Q: When is the return expression of a lambda expression executed?
Choose the number of the correct choice:
0) When the function returned by the lambda expression is called.
1) When you pass the lambda expression into another function.
2) When the lambda expression is evaluated.
3) When you assign the lambda expression to a name.
? 0
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # If Python displays <function...>, type Function, if it errors type Error, if it displays nothing type Nothing
>>> lambda x: x  # A lambda expression with one parameter x
? Function
-- OK! --

>>> a = lambda x: x  # Assigning a lambda function to the name a
>>> a(5)
? 5
-- OK! --

>>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
? 3
-- OK! --

>>> b = lambda x, y: lambda: x + y # Lambdas can return other lambdas!
>>> c = b(8, 4)
>>> c
? Function
-- OK! --

>>> c()
? 12
-- OK! --

>>> d = lambda f: f(4)  # They can have functions as arguments as well
>>> def square(x):
...     return x * x
>>> d(square)
? 16
-- OK! --

---------------------------------------------------------------------
Lambda the Free > Suite 2 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> # Try drawing an environment diagram if you get stuck!
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
? Error
-- OK! --

>>> higher_order_lambda(g)(2)
? 4
-- OK! --

>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)
? 3
-- OK! --

>>> print_lambda = lambda z: print(z) # When is the return expression of a lambda expression executed?
>>> print_lambda
? Function
-- OK! --

>>> one_thousand = print_lambda(1000)
? 1000
-- OK! --

>>> one_thousand # What did the call to print_lambda return? If it displays nothing, write Nothing
? Nothing
-- OK! --

---------------------------------------------------------------------
OK! All cases for Lambda the Free unlocked.

```

### Q4: Composite Identity Function

  ```python
  def composite_identity(f, g):
      """
      Return a function with one parameter x that returns True if f(g(x)) is
      equal to g(f(x)). You can assume the result of g(x) is a valid input for f
      and vice versa.
  
      >>> add_one = lambda x: x + 1        # adds one to x
      >>> square = lambda x: x**2          # squares x [returns x^2]
      >>> b1 = composite_identity(square, add_one)
      >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
      True
      >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
      False
      """
      "*** YOUR CODE HERE ***"
      return lambda x: f(g(x)) == g(f(x))
  ```

### Q5: Count Cond

```python
def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def f(n):
        i = 1
        count = 0
        while i <= n:
            if condition(n, i):
                count += 1
            i += 1
        return count
    return f
```

测试一下：

```shell
~/minghan/courses/CS61A/labs/lab02 % python3 ok -q count_cond --local
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Running tests

---------------------------------------------------------------------
Test summary
    1 test cases passed! No cases failed.

Cannot backup when running ok with --local.
~/minghan/courses/CS61A/labs/lab02 % python3 ok --score --local
=====================================================================
Assignment: Lab 2
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Lambda the Free
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
The Truth Will Prevail
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Higher Order Functions
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Doctests for count_cond

>>> from lab02 import *
>>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
>>> count_fives(10)   # 50 (10 * 5)
1
>>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
4
>>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
>>> count_primes = count_cond(is_i_prime)
>>> count_primes(2)    # 2
1
>>> count_primes(3)    # 2, 3
2
>>> count_primes(4)    # 2, 3
2
>>> count_primes(5)    # 2, 3, 5
3
>>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
8
Score: 1.0/1

---------------------------------------------------------------------
Doctests for composite_identity

>>> from lab02 import *
>>> add_one = lambda x: x + 1        # adds one to x
>>> square = lambda x: x**2          # squares x [returns x^2]
>>> b1 = composite_identity(square, add_one)
>>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
True
>>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
False
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    Lambda the Free: 0.0/0
    The Truth Will Prevail: 0.0/0
    Higher Order Functions: 0.0/0
    count_cond: 1.0/1
    composite_identity: 1.0/1

Score:
    Total: 2.0
```

### Optional

Q7: Multiple

```python
def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    mult_a, mult_b = a, b
    while mult_a != mult_b:
        if mult_a < mult_b:
            mult_a += a
        else:
            mult_b += b
    return mult_a
```

Q8: I Heard You Liked Functions...

一步步拆解即可，与其说是考察高阶函数，不如说是考察递归思维。

```python
def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def g(n):
        if n == 0:
            return lambda x: x
        if n == 1:
            return lambda x: f1(x)
        if n == 2:
            return lambda x: f2(f1(x))
        if n == 3:
            return lambda x: f3(f2(f1(x)))
        return lambda x: g(n-3)(f3(f2(f1(x))))
    return g
```

