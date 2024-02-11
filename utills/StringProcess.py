import re


def remove_special_characters_and_spaces(input_string):
    # Define the regular expression pattern to match special characters and spaces
    pattern = r'[^a-zA-Z0-9]'  # Matches any character that is not a letter or digit

    # Use the sub() function to replace all matches of the pattern with an empty string
    result_string = re.sub(pattern, '', input_string)

    return result_string
