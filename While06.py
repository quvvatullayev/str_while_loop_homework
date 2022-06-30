def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    s = str(s)
    i = 0
    sum = 0
    while i < len(s):

        if s[i].isalpha():

            if s[i].lower() == "a" or s[i].lower() == "o" or s[i].lower() == "e" or\
                s[i].lower() == "i" or s[i].lower() == "u":
                sum += 0
            
            else:
                sum += 1

        i += 1

    return sum

print(main("odevfsd"))