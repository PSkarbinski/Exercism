def rotate(text: str, key: int) -> str:
    alphabet = tuple[str]('abcdefghijklmnopqrstuvwxyz')
    cipher = alphabet[key:] + alphabet[0:key]
    cipherDict = dict[str, str](zip(alphabet, cipher))
    result = ''
    
    for char in text:
        if char.lower() not in alphabet:
            result += char
        else:
            cipherChar = cipherDict[char.lower()]
            result += cipherChar.upper() if char.isupper() else cipherChar
        
    return result