from typing import Literal

def classify(number: int) -> Literal['perfect', 'abundant', 'deficient']:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1: raise ValueError("Classification is only possible for positive integers.")

    aliquots = [num for num in range(1, number) if number % num == 0]
    aliquotsSum = sum(aliquots)

    return 'perfect' if number == aliquotsSum else 'abundant' if number < aliquotsSum else 'deficient'
    