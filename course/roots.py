import sys

def sqrt(x):
    """Comput teh square roots using the method 
    of Heron of Alexandria.
    
    Args:
        x: The number for which the square rot
           is to be computed. 
           
    Returns: 
        The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot compute square root "
                         f"of negative number {x}")

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ValueError as e:
        print(f"exception {e!r}")

if __name__ == '__main__':
    main()
