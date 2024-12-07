from numba import jit, TypingError


class EuclideanAlgorithmValueError(Exception):
    def __str__(self):
        return "Entered numbers must be greater than 0"


class EuclideanAlgorithmLengthError(Exception):
    def __str__(self):
        return ("The number of digits in the entered numbers "
                "should not exceed 20")


@jit(fastmath=True, cache=True)
def euclidean_algorithm_calculating(a: int, b: int
                            ) -> int | float | EuclideanAlgorithmValueError:
    if a <= 0 or b <= 0:
        raise EuclideanAlgorithmValueError
    elif b % a == 0 or a % b == 0:
        return a if a < b else b

    if a > b:
        a %= b
    elif b > a:
        b %= a

    while True:
        if a > b:
            a -= b
        elif b > a:
            b -= a

        if a == b:
            return a


def euclidean_algorithm(num1: int, num2: int
                            ) -> int | float | EuclideanAlgorithmLengthError:
    try:
        euclidean_algorithm_calculating(a=num1, b=num2)
    except TypingError:
        raise EuclideanAlgorithmLengthError
    else:
        return euclidean_algorithm_calculating(a=num1, b=num2)
