# Solution using for loop
def multiply_numbers_for(list_of_numbers : list) -> list :
    """
    Function to get a list of 5 numbers and returns a list
    of multiplied numbers by given constant, e.g. 2.

    Parameters
    -----------
    list_of_numbers : list
        List of numbers to be transformed.

    Returns
    --------
    transformed_list : list
        List of numbers that were multiplied by a constant.
    """

    CONSTANT_MULTIPLIER = 2

    if not len(list_of_numbers) == 5:
        raise('List should be exact length of 5')
    
    transformed_list = []
    for number in list_of_numbers:
        transformed_list.append(number*CONSTANT_MULTIPLIER)
    
    return transformed_list

test_list = [1,2,3,4,5]
# Test for solution
print(f'Solution using for loop. Before transformation: {test_list} after transformation:{multiply_numbers_for(test_list)}')

# Solution using list comprehension
def multiply_numbers_comprehension(list_of_numbers : list) -> list :
    """
    Function to get a list of 5 numbers and returns a list
    of multiplied numbers by given constant, e.g. 2.

    Parameters
    -----------
    list_of_numbers : list
        List of numbers to be transformed.

    Returns
    --------
    transformed_list : list
        List of numbers that were multiplied by a constant.
    """

    CONSTANT_MULTIPLIER = 2

    if not len(list_of_numbers) == 5:
        raise('List should be exact length of 5')
    
    transformed_list = [number*CONSTANT_MULTIPLIER for number in list_of_numbers]
    
    return transformed_list

test_list_2 = [2,4,6,8,10]
# Test comprehension solution
print(f'Solution using list comprehension. Before transformation: {test_list_2} after transformation:{multiply_numbers_comprehension(test_list_2)}')