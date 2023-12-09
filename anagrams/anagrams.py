def processed_string(text, reverse_function):
    if not isinstance(text, str):
        raise TypeError("The 'text' argument must be a string")

    if not callable(reverse_function):
        raise TypeError("The 'reverse_function' argument must be a function")

    if len(text) == 0:
        raise ValueError("The 'text' argument must be a string")

    words = text.split(' ')
    processed_words = [reverse_function(list(word)) for word in words]
    return ' '.join(''.join(word) for word in processed_words)


def reverse_only_letters(original_order):
    letters_stack = [char for char in original_order if char.isalpha()]

    for i in range(len(original_order)):
        if original_order[i].isalpha():
            original_order[i] = letters_stack.pop()

    return original_order


if __name__ == "__main__": #pragma: no cover
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ('!1abc', '!1cba')
    ]

    for text, reversed_text in cases:
        result = processed_string(text, reverse_only_letters)
        assert result == reversed_text, f"Expected: {reversed_text}, Got: {result}"
    print("Passes")