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
    for name in list_of_names:
        print(name)

# Test
names_list = ['andrzej', 'michal', 'wojciech']
print_names(names_list)