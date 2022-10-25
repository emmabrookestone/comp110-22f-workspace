"""An example of a list utility algorithm."""

# Name: contains
# Function with two parameters:
# needle- searching for
# haystack- what we're searching through
# return type: bool
def contains(needle: str, haystack: str) -> bool:
    # start from first index
    i: int = 0
    # looop through each index of list
    while 1 < len(haystack):
        #   test if the item at this index is equal to needle
        if haystack[1] == needle:
            #       test return true
            return True
        i += 1
    #return false
    return False