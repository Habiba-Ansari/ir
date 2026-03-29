def soundex(name):
    name = name.upper()

    # Step 1: Keep first letter
    first = name[0]

    # Step 2: Replace letters with numbers
    codes = {
        'B':1,'F':1,'P':1,'V':1,
        'C':2,'G':2,'J':2,'K':2,'Q':2,'S':2,'X':2,'Z':2,
        'D':3,'T':3,
        'L':4,
        'M':5,'N':5,
        'R':6
    }

    result = first

    # Step 3: Convert rest of letters
    for char in name[1:]:
        if char in codes:
            num = str(codes[char])
            if num != result[-1]:   # avoid duplicates
                result += num

    # Step 4: Remove vowels (already skipped)

    # Step 5: Make length 4
    result = result[:4].ljust(4, '0')

    return result


# Example
print(soundex("Robert"))
print(soundex("Rupert"))
