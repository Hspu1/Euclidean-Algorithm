from numba import jit

from euclidean_algorithm.euclidean_algorithm.exceptions import (
    EuclideanAlgorithmError
)


@jit(fastmath=True, cache=True)
def euclidean_algorithm(num1: int, num2: int) -> int | None:
    if num1 <= 0 or num2 <= 0:
        raise EuclideanAlgorithmError

    elif num1 == num2:
        return num1
    elif num1 == 1 or num2 == 1:
        return 1

    elif num2 % num1 == 0 or num1 % num2 == 0:
        return num1 if num1 < num2 else num2

    while True:
        if num1 > num2:
            while num1 > num2:
                num1 -= num2
        elif num2 > num1:
            while num2 > num1:
                num2 -= num1

        if num1 == num2:
            return num1
