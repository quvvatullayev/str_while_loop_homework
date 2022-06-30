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
    s = int(s)
    
    while i < n:
        if (s%10)%2 == 1:
            sum += s%10
        s //= 10
        i += 1

    return sum

print(main("75984235"))