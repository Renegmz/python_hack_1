"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    #...
    code = {
        'f': 'f',
        'o': '0',
        'z': 'z',
        'i': '1',
        'm': 'm',
        'a': '@',
        'n': 'n'
    }

    test = ""
    for carct in result:
        test += code.get(carct, " ")
    return test