"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    #...
    test = result[:len(result)-1]
    return test + result[len(result)-1].upper()