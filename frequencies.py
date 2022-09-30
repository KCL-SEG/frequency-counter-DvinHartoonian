"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    incomplete = True

    if len(items) == 0:
        return frequencies

    while incomplete:
        count = 0
        item = items[0]
        for i in list(items):
            if str(item) == str(i):
                count += 1
                items.remove(i)

        frequencies[str(item)] = count
        if len(items) == 0:
            incomplete = False

    return frequencies
