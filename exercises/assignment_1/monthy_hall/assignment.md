## Monthy-Hall
* Wikipedia link.

Description of the problem.

#### Input Format



#### Constraints


#### Output Format

Percentage of success/fail of door selection

#### Sample Input


#### Sample Output


#### Explanation

The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .
Hence,  is the Captain's room number.

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

# There is no need for changing the following lines.
# You can -- maybe should -- modify the following lines to test how it works.
#
# The following ('if') block runs when the module (`the_captains_room.py`)
# is called from the command line as
# ```
# $ python the_captains_room.py <input.txt>
# ```
#
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage:\n\t$ {} <input.txt>".format(sys.argv[0]))
        sys.exit()

    input_file = sys.argv[1]
    with open(input_file, 'r') as fp:
        # K = fp.readline()
        # rooms = fp.readline()
        # K = int(K)
        # rooms = [int(i) for i in rooms.split() if i]
        # output = run(K, rooms)
        # print("Captain's room number: {:d}".format(output))
        pass
```
