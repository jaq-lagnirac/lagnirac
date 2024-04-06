# Justin Caringal
def str_index_replace(original_string, replacement_char, change_index):
    """implements index replacement
    
    A function to organize individual char replacement for a string
    because Python strings are immutable
    
    Args:
        original_string (str): the reference string to be changed
        replacement_char (str): what to change it to
        index (int): the index to be replaced
        
    Returns:
        str: a new string altered with an altered character at index
    """

    # input validation
    if type(original_string) != str:
        print(f'original_string is not a string --> {original_string}')
        return None
    if type(replacement_char) != str:
        print(f'replacement_char is not a string --> {replacement_char}')
        return None
    if type(change_index) != int:
        print(f'change_index is not an integer --> {change_index}')
        return None

    new_string = '' # string to be added to and returned

    for index, character in enumerate(original_string):
        if index == change_index: # changes at the specific index
            new_string += replacement_char
        else: # rest of string remains the same
            new_string += character

    return new_string
