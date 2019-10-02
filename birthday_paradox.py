# The Birthday Paradox
# The Birthday Paradox (or Problem) concerns the probability
# of two randomly selected people having aniversary at the
# same date (https://en.wikipedia.org/wiki/Birthday_problem).
# Interesting enough, in a group of 70 people the probablity
# is of 99.9% that two persons are born on the same day of
# the year, and a 50% chance is reached with only 23 people.
#
# We want to check that by simulating birthdays and reading
# out those probabilities
#
# The ingredient of our algorithm are:
# - a group of N persons
# -- each person is a birthday
# - a random generator of birthdays
# - a checker for "cosmic-twins"
#
from random import randint

N_SIMULATIONS = 100

# Generate people
def generate_birthdays():
    """
    Return a list of random birthdays
    """
    birthdays = []
    for _ in range(n_persons):
        birthdays.append(randint(1, 365))
    return birthdays


# Check colliding birthdays
def check_birthdays(birthdays):
    """
    Return True if two birthdays collide
    """
    unique_birthdays = set(birthdays)
    return len(unique_birthdays) < len(birthdays)


#n_persons = 20
n_persons = int(input("Give me the number of people: "))

n_hits = 0
for i in range(N_SIMULATIONS):
    birthdays = generate_birthdays()
    have_twins = check_birthdays(birthdays)
    n_hits += int(have_twins)

print('{:f}'.format(n_hits/N_SIMULATIONS))
