def moveCharToEnd(text: str) -> str:
    return text[1:] + text[0]

def translate(text: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    splitText = text.split(' ')
    splitTextIndex = 0
    result = ''

    for word in splitText:
        index = 0
        if (not (word[0] in vowels or word[:2] == 'xr' or word[:2] == 'yt')):
            if ('qu' in word):
                while (not (word[0] in vowels) and word[:2] != 'qu'):
                    word = moveCharToEnd(word)
                if (word[:2] == 'qu'):
                    word = word[2:] + word[:2]
            elif ('y' in word and word[0] != 'y'):
                while (not (word[0] in vowels) and word[0] != 'y'):
                    word = moveCharToEnd(word)
            else:
                while (not (word[0] in vowels) and index < len(word)):
                    word = moveCharToEnd(word)
                    index += 1
        if (splitTextIndex == 0):
            result += word + 'ay'
        else:
            result += ' ' + word + 'ay'
        splitTextIndex += 1
    return result