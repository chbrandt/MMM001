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

    rooms_map = {}
    for room in rooms:
        try:
            rooms_map[room] += 1
        except:
            rooms_map[room] = 1
    for k,v in rooms_map.items():
        if v == 1:
            output = k
            break

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
        K = fp.readline()
        rooms = fp.readline()
        K = int(K)
        rooms = [int(i) for i in rooms.split() if i]
        output = run(K, rooms)
        print("Captain's room number: {:d}".format(output))
