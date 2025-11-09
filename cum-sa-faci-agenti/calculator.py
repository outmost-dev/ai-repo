from typing import List, Tuple, Optional


def calculate_average(numbers: List[float]) -> float:
    """Calculate the arithmetic mean of a list of numbers.

    Takes a list of numeric values and computes their average by dividing
    the sum of all values by the count of elements.

    Args:
        numbers: A list of numeric values (int or float). Must not be empty.

    Returns:
        The arithmetic mean as a float value.

    Raises:
        ZeroDivisionError: If the input list is empty.
        TypeError: If the list contains non-numeric values.

    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([10.5, 20.5, 30.0])
        20.333333333333332
        >>> calculate_average([100])
        100.0
    """
    total = sum(numbers)
    count = len(numbers)
    return total / count


def find_max_min(data: List[float]) -> Tuple[Optional[float], Optional[float]]:
    """Find the maximum and minimum values in a list.

    Searches through the provided list to identify both the largest and
    smallest values. If the list is empty, returns (None, None).

    Args:
        data: A list of numeric values (int or float). Can be empty.

    Returns:
        A tuple containing (max_value, min_value). Returns (None, None)
        if the input list is empty.

    Examples:
        >>> find_max_min([1, 5, 3, 9, 2])
        (9, 1)
        >>> find_max_min([42])
        (42, 42)
        >>> find_max_min([])
        (None, None)
        >>> find_max_min([-10, -5, -20, -1])
        (-1, -20)
    """
    if not data:
        return None, None
    return max(data), min(data)


def filter_even_numbers(numbers: List[int]) -> List[int]:
    """Filter and return only the even numbers from a list.

    Iterates through the input list and creates a new list containing
    only the numbers that are evenly divisible by 2 (even numbers).

    Args:
        numbers: A list of integer values to filter.

    Returns:
        A new list containing only the even numbers from the input list.
        Returns an empty list if no even numbers are found or if the
        input list is empty.

    Examples:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filter_even_numbers([1, 3, 5, 7])
        []
        >>> filter_even_numbers([2, 4, 6, 8])
        [2, 4, 6, 8]
        >>> filter_even_numbers([])
        []
        >>> filter_even_numbers([0, -2, -3, 10])
        [0, -2, 10]
    """
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
