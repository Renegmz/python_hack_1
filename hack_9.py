"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    #...
    iter = 0
    list_result = []
    while(iter <= len(result) - 1):
        list_result.append(result[iter])
        list_result.append('@')
        iter += 1
    return list_result
