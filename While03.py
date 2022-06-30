def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s = str(s)
    i = 0
    sum = 0
    while i < len(s):
        if s[i].isalpha() or s[i].isdigit():
            sum += 0
        else:
            sum += 1

        i += 1

    return sum

print(main("*o'798#9@cdvfsc64!^54&czb~`hoyh"))