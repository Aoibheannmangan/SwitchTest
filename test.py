def vowel(num):
    switch={
        1:'a',
        2:'e',
        3:'i',
        4:'o',
        5:'u',
    }
    return switch.get(num, "Invalid Input")

vowel(3)
vowel(0)