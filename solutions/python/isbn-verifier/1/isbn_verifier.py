def is_valid(isbn: str | int) -> bool:
    parsedISBN = str(isbn).replace('-', '').lower()
    if len(parsedISBN) != 10:
        return False
        
    validChars = [str(i) for i in range(10)]
    validChars.append('x')
    result: int = 0

    for i, char in enumerate[str](parsedISBN):
        if char not in validChars or (char == 'x' and i != 9):
            return False
        char = 10 if char == 'x' else char
        result += int(char) * (10 - i)
            
    return result % 11 == 0