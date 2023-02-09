def is_palindrome(word):
    """Return True if the word is a palindrome, False otherwise.

    Args:
    word (str): The word to check.

    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]
