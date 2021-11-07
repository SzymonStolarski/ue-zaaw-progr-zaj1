def print_names(list_of_names : list) -> None:
    """
    Function to print out elements from list (should be names :))

    Parameters
    ----------
    list_of_names : list
        List of names to be printed out in the console.

    Return
    -------
    None
    """
    if not len(list_of_names) == 5:
        raise('List should be exact length of 5')

    # one solution
    # for name in list_of_names:
    #     print(name)

    # comprehension list solution

    [print(name) for name in list_of_names]

# Test
names_list = ['andrzej', 'michal', 'wojciech', 'arek', 'benek']
print_names(names_list)