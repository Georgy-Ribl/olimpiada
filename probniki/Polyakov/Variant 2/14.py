from other import defines

s = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
s = defines.conv(str(s), 10, 9)
print(s.count('8'))
