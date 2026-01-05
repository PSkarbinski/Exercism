def is_pangram(sentence: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lowercaseSentence = sentence.lower()

    for char in alphabet:
        if char not in lowercaseSentence:
            return False
    return True
