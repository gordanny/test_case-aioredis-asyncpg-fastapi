def check_anagrams(string_1, string_2):
    """Checking if strings are anagrams."""
    check = sorted(string_1.lower()) == sorted(string_2.lower())
    return check
