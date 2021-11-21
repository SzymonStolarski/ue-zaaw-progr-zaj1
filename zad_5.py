def check_if_element_in_list(
                            list_to_check: list,
                            element_to_check: int) -> bool:
    return element_to_check in list_to_check


# Test
print(check_if_element_in_list([1, 2, 3], 10))
