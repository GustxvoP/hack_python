"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    for k in range (6):
        result.append(k)    
    return result
print(fn_hack_6())