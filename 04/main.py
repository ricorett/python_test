def concatenation(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise TypeError("Both arguments must be strings")
    return string1 + string2
