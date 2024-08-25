import re

pattern = re.compile(r'^[a-zA-Z0-9!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`~\-]{8,}$')

test_strings = [
    "abcd1234",          # Valid
    "12345678",          # Valid
    "!@#ABCdef",         # Valid
    "a1!",               # Invalid (less than 8 characters)
    "abcdefgh",          # Valid
    "1234!@#$",          # Valid
    "A1b2C3d4E5f6g7h8i9",# Valid
]

for s in test_strings:
    if pattern.fullmatch(s):
        print(f'Valid: {s}')
    else:
        print(f'Invalid: {s}')