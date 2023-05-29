"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    #...
    index = 5
    while(index >= 0):
        result.append(index)
        index -= 1
    return result