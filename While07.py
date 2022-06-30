def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    sum = 0
    i = 0
    n = len(str(s))
    
    while i < n:
        if (s%10)%2 == 0:
            sum += 1
        s //= 10
        i += 1

    return sum

print(main(759))