# Run tests

To run tests over the delivered solutions one should be able to do from this directory:
```
$ pytest [-s] the_captains_room/
```
, in the particular (example) case of _the captain's room_ exercise.

The current [pytest](https://docs.pytest.org/en/latest/) implemented in this example
-- defined in `the_captains_room/test_the_captains_room.py` -- has three test functions
allocated:

* input/output correctness (implemented);
* pep-8/lint format (**to be implemented**);
* docs coverage (**to be implemented**).

In the assignment I ask for a function `run()` to be defined, where "`run`" will 
get the input arguments and return an output -- `run()` is _all_ the matters from 
the testing point-of-view. The way "`run`" solves the exercise is not of pytest'
business.

To have each student's solution tested/verified it should be sufficient to just put
his/her python module in the corresponding directory -- For instance, just overwrite
"`the_captains_room.py`" module with the student's.
