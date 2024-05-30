def create_dict(s):
    result = {}
    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


s1, s2 = map(create_dict, input().split())
k = 0

for char in s2:
    if char not in s1:
        k += s2[char]
    elif s1[char] < s2[char]:
        k += s2[char] - s1[char]
print(k)
