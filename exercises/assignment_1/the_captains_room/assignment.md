## The Captain's Room
* from Hackerrank:
    * https://www.hackerrank.com/challenges/py-the-captains-room/problem

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
* A Captain.
* An unknown group of families consisting of $K$ members per group where $K \neq 1$.

_The Captain was given a separate room, and the rest were given one room per group._

Mr. Anant has an *unordered* list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear $K$ times per group _except_ for the Captain's room.

_Mr. Anant needs you to help him find the Captain's room number._
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of $K$ and the room number list.


#### Input Format

The first line consists of an integer, $K$, the size of each group.
The second line contains the unordered elements of the room number list.


#### Constraints

$$ 1 < K < 1000 $$

#### Output Format

Output the Captain's room number.

#### Sample Input

```
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
```

#### Sample Output

```
8
```

#### Explanation

The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .
Hence,  is the Captain's room number.

### Exercise

Define a function `run(K, rooms)` in a file `the_captains_room.py` with the following structure:
```python
'''
The Captain's room

Notes:
* <any notes about the problem>
'''

author = '<your-name-here>'

# Imports, other function definition, global variables and anything else
# you feel is useful to implement the solution can be done/defined here.


def run(K, rooms):
    '''
    Print the Captain's room number

    * K: integer
        number of tourists in each group
    * rooms: list of integers
        room number of each tourist
    '''
    output = None

    # do stuff; define 'output' properly.

    return output

```
