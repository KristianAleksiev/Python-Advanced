expression = input()

opening_brackets = []
pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}

balanced = True

for char in expression:

    if char in "([{":
        opening_brackets.append(char)

    elif not opening_brackets:
        balanced = False  # No opening brackets

    else:
        last_opening_bracket = opening_brackets.pop()
        if pairs[last_opening_bracket] != char:
            balanced = False

    if not balanced:
        break

if not balanced or opening_brackets:
    print("NO")
else:
    print("YES")
