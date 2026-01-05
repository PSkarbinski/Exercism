def moveCharToEnd(text: str) -> str:
    return text[1:] + text[0]

def translate(text: str) -> str:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}
    SPECIALS = {'xr', 'yt'}
    result = []

    for word in text.split():
        index = 0
        if (not (word[0] in VOWELS or word[:2] in SPECIALS)):
            while (not (word[0] in VOWELS) and index < len(word)):
                if (word[:2] == 'qu'):
                    word = word[2:] + word[:2]
                    break
                if (word[0] == 'y' and index != 0):
                    break
                word = moveCharToEnd(word)
                index += 1    
        result.append(word + 'ay')
    return ' '.join(result)