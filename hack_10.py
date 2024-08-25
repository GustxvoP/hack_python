"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def mayus(characters):
    return characters.upper()

def conv(characters):
    characters = characters.replace('o', '0')
    characters = characters.replace('i', '1')
    characters = characters.replace('a', '@')
    return characters

def fn_hack_10():
    result = "fooziman"
    result = [conv(character) for character in result]
    result = [mayus(character) for character in result]
    return result

print(fn_hack_10())