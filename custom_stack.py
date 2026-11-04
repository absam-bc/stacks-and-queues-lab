def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    stack = []

    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for character in s:
        if character in '({[':
            stack.append(character)

        elif character in ')}]':
            if not stack:
                return False

            last_opening = stack.pop()

            if last_opening != matching_brackets[character]:
                return False

    return len(stack) == 0
