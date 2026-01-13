def is_isogram(string: str) -> bool:
    letters: list[str] = []
    
    for char in string.lower():
        if char not in ['-', ' '] and char in letters:
            return False
        letters.append(char)

    return True
