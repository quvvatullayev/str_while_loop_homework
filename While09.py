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
    s = int(s)
    
    while i < n:
        sum += s%10
        s //= 10
        i += 1

    return sum

print(main("75901"))