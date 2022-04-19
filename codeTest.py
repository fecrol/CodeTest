"""
Author: Maciej Fec
Email: maciejfec1996@gmail.com

The problem:
In a language of your choice, using all best practice principles you’re aware of, could you please provide code that iterates in multiples of A until X, then in multiples of A + 1 until 2X, then multiples of A + 2 until 3X. Please state any assumptions you’ve made.

My assumptions:
- X cannot always be included, hence in some cases the final number will be less than, but as close to X as possible.
- If A is 0, result is 0.
- X cannot be less than A.
- A and/or X cannot be floats
"""

def multiples_of_a_until_x(a, x):
    """
    Returns a list of numbers multiplied by A up to and including X if possible to include X
    """

    if a == 0:
        return 0
    
    if x < a or not isinstance(a, int) or  not isinstance(x, int):
        # Returns -1 to indicate error if X is less than A
        return -1
    
    return [n * a for n in range(1, x + 1) if n * a <= x]

def display_solution(a, x):
    """
    Prints a list of numbers from A until X, then in multiples of A + 1 until 2X, 
    then multiples of A + 2 until 3X
    """
    
    result = multiples_of_a_until_x(a, x)

    if result == -1:
        print("A and/or X are invalid")
    else:
        for i in range(3):
            """
            Adds i to a and multiplies x by i + 1 three times 
            to achieve the outcome of A until X, A + 1 until 2X, and A + 2 until 3X
            """
            print(multiples_of_a_until_x(a + i, x * (i + 1)))