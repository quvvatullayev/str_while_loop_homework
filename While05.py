def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s = str(s)
    i = 0
    sum = 0
    while i < len(s):

        if s[i].isalpha():

            if s[i] == s[i].lower():
                sum += 1

        i += 1

    return sum

print(main("DlkjoiSImngjhsc56O"))