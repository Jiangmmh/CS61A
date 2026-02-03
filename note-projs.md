## Timeline

- 2026.02.03 完成proj1
- 

## Proj1 The Game of Hog

在这个项目中，我们将编写一个Hog游戏的模拟程序。规则如下：

- 有两个玩家来玩这个游戏，初始分数均为0

- 每个玩家依次选择希望投掷的骰子数，将这些骰子点数之和增加到玩家分数中

- 特殊规则：

  - **Sow Sad**，如果投掷的骰子中有一个为1，则该轮得分为1
  - **Boar Brawl**，如果玩家可以选择投掷0个骰子，分数增加对手分数十位数和自己分数的个位数的绝对值的三倍，如果该值为0，则增加1
  - **Sus Fuss**，如果在投掷完骰子之后，当前玩家的分数为3或4的倍数，则分数直接增加到下一个质数

  ### Problem 0 (0 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 00 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 0 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
? 4
-- OK! --

>>> test_dice() # Second call
? 1
-- OK! --

>>> test_dice() # Third call
? 2
-- OK! --

>>> test_dice() # Fourth call
? 4
-- OK! --

---------------------------------------------------------------------
Question 0 > Suite 2 > Case 1
(cases remaining: 1)

Q: Which of the following is the correct way to "roll" a fair, six-sided die?
Choose the number of the correct choice:
0) make_fair_dice(6)
1) six_sided
2) make_test_dice(6)
3) six_sided(1)
4) six_sided()
5) six_sided(6)
? 4
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 0 unlocked.
```

### Problem 1 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 01 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 1
(cases remaining: 59)

>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
? 10
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 2
(cases remaining: 58)

>>> from hog import *
>>> roll_dice(3, make_test_dice(4, 6, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 3
(cases remaining: 57)

>>> from hog import *
>>> roll_dice(4, make_test_dice(2, 2, 3))
? 9
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 4
(cases remaining: 56)

>>> from hog import *
>>> a = roll_dice(4, make_test_dice(1, 2, 3))
>>> a # check that the value is being returned, not printed
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 5
(cases remaining: 55)

>>> from hog import *
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
? 1
-- OK! --

>>> # Make sure you call dice exactly num_rolls times!
>>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
>>> # Note that a return statement within a loop ends the loop
>>> roll_dice(1, counted_dice)
? 6
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 1 unlocked.
```

实现roll_dice函数：

```python
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. Defaults to the six sided dice.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    total_score = 0
    flag = False
    while num_rolls > 0:
        score = dice()
        if score == 1:
            flag = True
        total_score += score
        num_rolls -= 1
    
    if flag:
        return 1
    return total_score
    # END PROBLEM 1
```

注意不要为了效率，在掷出1后直接break出循环，因为这会影响dice函数后续的返回值。

### Problem 2 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 02 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 1
(cases remaining: 14)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(21, 46)
? 9
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 2
(cases remaining: 13)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(52, 79)
? 15
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 3
(cases remaining: 12)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(0, 0)
? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 4
(cases remaining: 11)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(0, 5)
? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 5
(cases remaining: 10)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(2, 5)
? 6
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 6
(cases remaining: 9)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(7, 2)
? 21
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 7
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 8
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 9
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 10
(cases remaining: 5)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(72, 29)
? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 11
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 12
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 13
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 14
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 2 unlocked.
```

实现boar_brawl策略：

```python
def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    s1 = opponent_score // 10 % 10
    s2 = player_score % 10
    return max(1, abs(s1 - s2) * 3)
    # END PROBLEM 2
```

### Problem 3 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 03 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 1
(cases remaining: 12)

>>> from hog import *
>>> take_turn(2, 7, 27, make_test_dice(4, 5, 1))
? 11
-- Not quite. Try again! --

? 9
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 2
(cases remaining: 11)

>>> from hog import *
>>> take_turn(3, 15, 9, make_test_dice(4, 6, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 3
(cases remaining: 10)

>>> from hog import *
>>> take_turn(0, 12, 41) # what happens when you roll 0 dice?
? 6
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 4
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 5
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 6
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 7
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 8
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 9
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 10
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 11
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 3 unlocked.
```

实现take_turn函数，在其中不要使用`Sus Fuss`策略：

```python
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    score = 0
    if num_rolls == 0:
        score += boar_brawl(player_score, opponent_score)
    else:
        score = roll_dice(num_rolls, dice)
    return score
    # END PROBLEM 3
```

### Problem 4 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 04 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 1
(cases remaining: 27)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(1)
? 1
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 2
(cases remaining: 26)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 3
(cases remaining: 25)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(3)
? 2
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 4
(cases remaining: 24)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(9)
? 3
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 5
(cases remaining: 23)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(28)
? 6
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 6
(cases remaining: 22)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(64)
? 7
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 7
(cases remaining: 21)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 8
(cases remaining: 20)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(97)
? 2
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 9
(cases remaining: 19)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 10
(cases remaining: 18)

>>> from hog import *
>>> import tests.construct_check as test
>>> sus_points(1)
? 1
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 11
(cases remaining: 17)

>>> from hog import *
>>> import tests.construct_check as test
>>> sus_points(21)
? 23
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 4 unlocked.
```

实现num_factors、sus_points和sus_update：

```python
def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    num_factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            num_factors += 1
    return num_factors
    # END PROBLEM 4

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    n_factors = num_factors(score)
    if n_factors == 3 or n_factors == 4:
        score += 1
        while not is_prime(score):
            score += 1
    return score
    # END PROBLEM 4

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return sus_points(score)
    # END PROBLEM 4
```

### Problem 5 (4 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 05 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 1
(cases remaining: 104)

Q: The variables score0 and score1 are the scores for Player 0
and Player 1, respectively. Under what conditions should the
game continue?
Choose the number of the correct choice:
0) While score1 is less than goal
1) While score0 is less than goal
2) While score0 and score1 are both less than goal
3) While at least one of score0 or score1 is less than goal
? 2
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 2
(cases remaining: 103)

Q: What is a strategy in the context of this game?
Choose the number of the correct choice:
0) The number of dice a player will roll
1) A player's desired turn outcome
2) A function that returns the number of dice a player will roll
? 2
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 3
(cases remaining: 102)

Q: If strategy1 is Player 1's strategy function, score0 is
Player 0's current score, and score1 is Player 1's current
score, then which of the following demonstrates correct
usage of strategy1?
Choose the number of the correct choice:
0) strategy1(score0, score1)
1) strategy1(score1, score0)
2) strategy1(score1)
3) strategy1(score0)
? 1
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 4
(cases remaining: 101)

Q: Player 0 has a score of 55, Player 1 has a score of 22,
and Player 0's strategy is given by lambda x, y: ((y % 10) * (x % 10)) % 10.
How many dice will Player 0 roll on their turn?
Choose the number of the correct choice:
0) 10
1) 0
2) 5
3) 1
? 1
-- OK! --
```

实现play函数：

```python
def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            num_roll = strategy0(score0, score1)
            score0 = update(num_roll, score0, score1, dice)
        else:
            num_roll = strategy1(score1, score0)
            score1 = update(num_roll, score1, score0, dice)
        who = abs(who - 1)
    # END PROBLEM 5
    return score0, score1
```

### Problem 6 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 06 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> always_roll(3)(10, 20)
? 3
-- OK! --

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 2
(cases remaining: 1)

>>> from hog import *
>>> always_roll(0)(99, 99)
? 0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 6 unlocked.
```

实现always_roll：

```python
def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    return lambda x, y: n
    # END PROBLEM 6
```

### Problem 7 (2 pt)

实现is_always_roll函数，该函数的作用是检查strategy对任何输入都有着相同的输出值：

```python
def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    prev = 0
    for score in range(0, goal):
        for opponent_score in range(0, goal):
            num_roll = strategy(score, opponent_score)
            if (score != 0 or opponent_score != 0) and prev != num_roll:
                return False
            prev = num_roll
    return True
    # END PROBLEM 7
```

### Problem 8 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 08 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 8 > Suite 1 > Case 1
(cases remaining: 7)

Q: What is one reason that make_averaged is a higher order function?
Choose the number of the correct choice:
0) It contains a nested function
1) It calls a function that is not itself
2) It takes in a function as an argument
3) It uses the *args keyword
? 2
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 1 > Case 2
(cases remaining: 6)

Q: How many arguments does the function passed into make_averaged take?
Choose the number of the correct choice:
0) None
1) Two
2) An arbitrary amount, which is why we need to use *args to call it
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) None
1) Two
2) An arbitrary amount, which is why we need to use *args to call it
? 2
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 2 > Case 1
(cases remaining: 5)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_dice = make_averaged(dice, 1000)
>>> # Average of calling dice 1000 times
>>> averaged_dice()
? 3.75
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 2 > Case 2
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_roll_dice = make_averaged(roll_dice, 1000)
>>> # Average of calling roll_dice 1000 times
>>> # Enter a float (e.g. 1.0) instead of an integer
>>> averaged_roll_dice(2, dice)
? 6.0
-- OK! --
```

注意roll_dice的实现中，如果掷出1，则返回的分数也为1。

实现`make_averaged`函数：

```python
def make_averaged(original_function, times_called=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TIMES_CALLED times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def f(*args):
        score = 0
        for i in range(times_called):
            score += original_function(*args)
        return score / times_called
    return f
    # END PROBLEM 8
```

这里使用了python的可变参数，使用`*args`来表示可变参数，而`original_function(*args)`表示转发参数。

### Problem 9 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 09 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 9 > Suite 1 > Case 1
(cases remaining: 10)

Q: If multiple num_rolls are tied for the highest scoring
average, which should you return?
Choose the number of the correct choice:
0) The lowest num_rolls
1) The highest num_rolls
2) A random num_rolls
? 0
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 1
(cases remaining: 9)

>>> from hog import *
>>> dice = make_test_dice(3)   # dice always returns 3
>>> max_scoring_num_rolls(dice, times_called=1000)
? 10
-- OK! --


---------------------------------------------------------------------
Question 9 > Suite 3 > Case 1
(cases remaining: 6)

>>> from hog import *
>>> dice = make_test_dice(2)     # dice always rolls 2
>>> max_scoring_num_rolls(dice, times_called=1000)
? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 2
(cases remaining: 5)

>>> from hog import *
>>> dice = make_test_dice(1)     # dice always rolls 1
>>> max_scoring_num_rolls(dice, times_called=1000)
? 1
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 3
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
>>> max_scoring_num_rolls(dice, times_called=1000)
? 1
-- OK! --
```

实现`max_scoring_num_rolls`函数：

```python
def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    averaged_roll_dice = def max_scoring_num_rolls(dice=six_sided, times_called=1000):
    """Return the number of dice (1 to 10) that gives the maximum average score for a turn.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    averaged_roll_dice = make_averaged(roll_dice, times_called)
    max_score = 0
    num_rolls = 1
    for i in range(1, 11):
        score = averaged_roll_dice(i, dice)
        if score > max_score:
            max_score = score
            num_rolls = i
    return num_rolls
    # END PROBLEM 9(roll_dice, times_called)
    max_score = 0
    num_rolls = 1
    for i in range(1, 11):
        score = averaged_roll_dice(i, dice)
        if score > max_score:
            max_score = score
            num_rolls = i
    return num_rolls
    # END PROBLEM 9
```

- 首先使用`make_averaged`构造一个`averaged_roll_dice`
- 然后循环遍历尝试投掷 1～10个骰子，使用max_score记录投掷得到的最大score，num_rolls记录最大score对应的骰子数

### Problem 10 (2 pt)

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 10 -u --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 1
(cases remaining: 10)

>>> from hog import *
>>> boar_strategy(40, 51, threshold=7, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 2
(cases remaining: 9)

>>> from hog import *
>>> boar_strategy(40, 51, threshold=15, num_rolls=7)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 3
(cases remaining: 8)

>>> from hog import *
>>> boar_strategy(40, 51, threshold=16, num_rolls=7)
? 7
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 4
(cases remaining: 7)

>>> from hog import *
>>> boar_strategy(44, 53, threshold=3, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 5
(cases remaining: 6)

>>> from hog import *
>>> boar_strategy(44, 53, threshold=4, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 6
(cases remaining: 5)

>>> from hog import *
>>> boar_strategy(40, 31, threshold=9, num_rolls=5)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 7
(cases remaining: 4)

>>> from hog import *
>>> boar_strategy(40, 31, threshold=10, num_rolls=5)
? 5
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 8
(cases remaining: 3)

>>> from hog import *
>>> boar_strategy(40, 52, threshold=15, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 9
(cases remaining: 2)

>>> from hog import *
>>> boar_strategy(40, 52, threshold=16, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 10
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 10 unlocked.
```

实现boar_strategy函数：

```python
def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    score = boar_brawl(score, opponent_score)
    if score >= threshold:
        return 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10
```

### Problem 11 (2 pt)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~shell
~/minghan/courses/CS61A/projs/hog % python3 ok -q 11 -u --local
Assignment: Project 1: Hog
OK, version v1.18.1
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 1
(cases remaining: 8)

>>> from hog import *
>>> sus_strategy(31, 21, threshold=10, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 2
(cases remaining: 7)

>>> from hog import *
>>> sus_strategy(30, 41, threshold=10, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 3
(cases remaining: 6)

>>> from hog import *
>>> sus_strategy(53, 60, threshold=14, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 4
(cases remaining: 5)

>>> from hog import *
>>> sus_strategy(53, 60, threshold=15, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 5
(cases remaining: 4)

>>> from hog import *
>>> sus_strategy(23, 54, threshold=4, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 6
(cases remaining: 3)

>>> from hog import *
>>> sus_strategy(14, 21, threshold=8, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 7
(cases remaining: 2)

>>> from hog import *
>>> sus_strategy(14, 21, threshold=12, num_rolls=5)
? 5
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 8
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 11 unlocked.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

实现sus_strategy函数：

```python
def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    updated_score = sus_update(0, score, opponent_score)
    if updated_score - score >= threshold:
        return 0
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11
```

测试一下：

```shell
~/minghan/courses/CS61A/projs/hog % python3 ok --score --local
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Question 0
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 1
    Passed: 3
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 2
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 3
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 4
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 5
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 6
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 7
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 8
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 9
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 10
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 11
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Question 12
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Point breakdown
    Question 0: 0.0/0
    Question 1: 2.0/2
    Question 2: 2.0/2
    Question 3: 2.0/2
    Question 4: 2.0/2
    Question 5: 4.0/4
    Question 6: 2.0/2
    Question 7: 2.0/2
    Question 8: 2.0/2
    Question 9: 2.0/2
    Question 10: 2.0/2
    Question 11: 2.0/2
    Question 12: 0.0/0

Score:
    Total: 24.0
```

总结：一个挺有意思的小项目，难度不大，考察的都是前面几节课程中学到的知识点，挺好玩的。

## 