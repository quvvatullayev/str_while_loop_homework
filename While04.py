def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s = str(s)
    i = 0
    sum = 0
    while i < len(s):
        if s[i] == s[i].upper():
            sum += 1

        i += 1

    return sum

print(main("DlkjoiSImngjhO"))