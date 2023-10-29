from difflib import SequenceMatcher

# Use string similarity to find videos in the channel
def find_most_similar(input_str, string_list):
    """
    Finds the most similar string in the list to the input string using SequenceMatcher.
    
    Parameters:
        - input_str (str): The string to be compared.
        - string_list (list of str): The list of strings to compare against.
    
    Returns:
        - The string in string_list most similar to input_str.
    """
    max_ratio = -1
    most_similar_string = None

    for s in string_list:
        ratio = SequenceMatcher(None, input_str, s).ratio()
        if ratio > max_ratio:
            max_ratio = ratio
            most_similar_string = s

    return most_similar_string