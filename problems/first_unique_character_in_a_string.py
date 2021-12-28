"""
    Given a string input_string, find the first non-repeating character in it and return its index.
    If it does not exist, return -1.
"""


from collections import OrderedDict


def first_unique_in_character_in_a_string(input_string):
    """2 pass with ordered hash"""
    ordered_dict = OrderedDict()
    for i, character in enumerate(input_string):
        if character not in ordered_dict:
            ordered_dict[character] = [i]
        else:
            ordered_dict[character].append(i)

    for character in ordered_dict:
        if len(ordered_dict[character]) == 1:
            return ordered_dict[character][0]

    return -1
