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
    n = len(s)
    
    while i < n:
        if str(s[i]).isdigit():
            if int(s[i])%2 == 0:
                sum += 1
        i += 1
    return sum

print(main("75984"))