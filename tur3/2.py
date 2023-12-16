import json


def translate(text):
    russian_chars = "йцукенгшщзхъфывапролджэячсмитьбюё"
    english_chars = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
    alphabet = dict(zip(russian_chars, english_chars))
    ans = ''.join(alphabet.get(char, char) for char in text.lower())
    return ans


s = r'\\'
s += input()
s = json.loads(f'"{s[1::]}"')
ans = translate(s)
print(ans)
