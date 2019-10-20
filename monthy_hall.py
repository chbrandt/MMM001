# The Monty-Hall problem
# * https://en.wikipedia.org/wiki/Monty_Hall_problem
#
# The Monty-Hall problem consists on an statistical problem
# where the following situation is proposed:
# > you're on a game show where you're offered three closed
# > doors and asked to pick one; behind one of those doors
# > there is a prize, the remaining two have nothing. After
# > you pick one the host removes one of the remaing two
# > from the game and asks if you want to change your previous
# > choice. Note that the door just eliminated by the host
# > is *certain* to not be the one hiding the prize.
# The question proposed then is "should you change your
# previously chosen door or not?".
#
# Considering the choice done at first -- among three doors --
# is completely random, the chances of choosing the "right"
# door is of 1/3. On your second choice -- now over two doors
# only --, what are the chances of winning the prize either
# by sticking to the first choice or changing to the other one?
#
# The right answer to this question -- statistically proved --
# is "yes, you should change the door when asked to you,
# after the elimination of a/the third door". And the reason
# is because the probaility of finding the prize behind the
# "other" door is of 2/3 now.
#
# To most of the people, including me, this result is not
# easy to accept. To check that, we can simulate the game
# and verify the results.
#
# Algorithm
# ---------
# * Generate three options: "prize", "none", "none"
# * Choose one: "i"
# * Remove a/the "none" option from remaining options
# * In 50% of the cases, change the original options,
#   * Stay with initial option in the other 50% cases
# * Check is chosen door is the "prize" or "none"
# * Accumulate the number of "prize" from each simulation
# * Simulate the process N times
# * Print the fraction of "prizes" and "none" in total

N_SIMULATIONS = 1000

def generate_doors():
    from random import shuffle
    doors = [True, None, None]
    shuffle(doors)
    return doors

def pick_one():
    from random import randint
    return randint(0,2)

def remove_one(doors, chosen_one):
    l = [i for i in range(3) if i != chosen_one]
    if doors[l[0]] is None:
        return l[0]
    else:
        assert doors[l[1]] is None
        return l[1]


CHANGE=False
def should_change():
    try:
        return bool(CHANGE)
    except:
        return False

N_PRIZES = 0
N_LOSTS = 0

for i in range(N_SIMULATIONS):
    doors = generate_doors()
    chosen_door = pick_one()
    remove_door = remove_one(doors, chosen_door)
    doors[remove_door] = False
    if should_change():
        if doors[chosen_door] is True:
            N_LOSTS += 1
        else:
            N_PRIZES += 1
    else:
        if doors[chosen_door] is True:
            N_PRIZES += 1
        else:
            N_LOSTS += 1


assert N_PRIZES + N_LOSTS == N_SIMULATIONS
print('{:.2f}'.format(N_PRIZES/N_SIMULATIONS))
