class EuclideanAlgorithmValueError(Exception):
    def __str__(self):
        return "Entered numbers must be greater than 0"


class EuclideanAlgorithmLengthError(Exception):
    def __str__(self):
        return ("The number of digits in the entered numbers "
                "should not exceed 20")
