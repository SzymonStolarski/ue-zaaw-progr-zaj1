def transform_two_lists(list_1: list, list_2: list) -> list:
    POWER = 3

    merged_no_duplicates_list = list(set(list_1 + list_2))
    powered_list = [element**POWER for element in merged_no_duplicates_list]
    return powered_list


# Test
print(transform_two_lists([1, 2, 3], [3, 4, 5]))
