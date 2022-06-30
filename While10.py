def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum = 0
    i = 0
    n = len(s)
    
    while i < n:
        if int(s[i])%2 == 1:
            sum += int(s[i])
        i += 1

    return sum

print(main("78513"))