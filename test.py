import re

with open("tests/math/arithmetics.ly", 'r') as f:
    code = f.read()
    code = re.sub(r'/\*.*?\*/|(?s)/\\*.*?\\*/|#.*|#//.*', '', code)

print(code)
