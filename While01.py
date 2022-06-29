def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """

    n = 0
    y = 0
    while n < len(s):
        if s[n].isdigit():
            y += 1
        n += 1
 
    return y

print(main("df5f6"))