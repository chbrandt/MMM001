# This is a test module for 'pytest', to run it:
# ```
# $ pytest <this-module.py or directory>
# ```
# If you want pytest to print eventual 'print' statements:
# ```
# $ pytest <this-module.py or directory> -s
# ```
#
import the_captains_room
from the_captains_room import author, run

from os import path
_here = path.dirname(__file__)

INPUT_FILE = path.join(_here, 'input','test.txt')
OUTPUT_FILE = path.join(_here, 'output','test.txt')

def _read_input_test(fp):
    N = fp.readline()
    D = fp.readline()
    return (N,D)

def _read_output_test(fp):
    O = fp.readline()
    return O

def test_output():
    with open(INPUT_FILE, 'r') as fi, \
         open(OUTPUT_FILE, 'r') as fo:
        while True:
            in_test = _read_input_test(fi)
            out_test = _read_output_test(fo)
            if not out_test.strip():
                break
            in_test = (int(in_test[0]),
                       [int(i) for i in in_test[1].strip().split()])
            out_test = int(out_test.strip())

            out_run = run(*in_test)

            msg = "Fail: Was expecting '{!s}', got '{!s}' instead."
            #TODO: we should assert the 66(True)/33(False) percentage
            assert out_run == out_test, msg.format(out_test, out_run)
            msg = "\nPass:\n\tinput '{}'\n\toutput '{}'"
            print(msg.format(in_test, out_test))


# def test_lint():
#     """
#     Check for pep-8/lint standards
#     """
#     raise NotImplementedError
#     # return True
#
#
# def test_docs():
#     """
#     Check for docs coverage
#     """
#     raise NotImplementedError
#     # return True


# if __name__ == '__main__':
#     test_output()
