## Monthy-Hall
* https://en.wikipedia.org/wiki/Monty_Hall_problem

The Monty-Hall problem consists on an statistical problem
where the following situation is proposed:

> you're on a game show where you're offered three closed
> doors and asked to pick one; behind one of those doors
> there is a prize, the remaining two have nothing. After
> you pick one the host removes one of the remaing two
> from the game and asks if you want to change your previous
> choice. Note that the door just eliminated by the host
> is *certain* to not be the one hiding the prize.

The question proposed then is "should you change your
previously chosen door or not?".

Considering the choice done at first -- among three doors --
is completely random, the chances of choosing the "right"
door is of 1/3. On your second choice -- now over two doors
only --, what are the chances of winning the prize either
by sticking to the first choice or changing to the other one?

The right answer to this question -- statistically proved --
is "yes, you should change the door when asked to you,
after the elimination of a/the third door". And the reason
is because the probaility of finding the prize behind the
"other" door is of 2/3 now.

To most of the people, including me, this result is not
easy to accept. To check that, we can simulate the game
and verify the results.

#### Input Format

The problem accepts onw simple input: either `True`, or `1` for when the simulation with the player choosing to, yes, change the door at the second choice. Either `False` or `0` to simulate when the player doesn't change the doors.


#### Requirements

The simulation should be executed at least 10000 times.

#### Output Format

Percentage of success/fail of door select (with/without prize).

#### Sample Input

1

#### Sample Output

66.66

#### Explanation

The probaility of finding the prize behind the
"other" (second) door is of 2/3.

### Exercise

Define a function `run(should_change)` that simulates the process 10000 times,
in a file `monthy_hall.py` with the following structure:
```python
'''
Monthy Hall

Notes:
* <any notes about the problem>
'''

author = '<your-name-here>'

# Imports, other function definition, global variables and anything else
# you feel is useful to implement the solution can be done/defined here.


def run(should_change):
    '''
    Print the percentage of success

    '''
    output = None

    # do stuff; define 'output' properly.

    return output

```
