def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum = 0
    i = 0
    n = len(s)
    
    while i < n:
        if str(s[i]).isdigit():
            sum += int(s[i])
        i += 1

    return sum

print(main("sf8f9f6d"))