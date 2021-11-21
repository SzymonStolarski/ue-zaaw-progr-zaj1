def sum_of_numbers_comparator(
                                first_number: int,
                                second_number: int,
                                third_number: int) -> bool:
    return sum([first_number, second_number]) >= third_number


# Test
print(sum_of_numbers_comparator(1, 5, 4))
