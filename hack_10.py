"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    #...
    code = {
        'f': 'F',
        'o': '0',
        'z': 'Z',
        'i': '1',
        'm': 'M',
        'a': '@',
        'n': 'N'
    }
    list_result = []
    for caract in result:
        list_result.append(code.get(caract,""))
    return list_result