n = input()
arr_znk = [s for s in n if s in '+-*']
alphabet = [[int(i) for i in input().split()] for j in range(5)]
alf_arr_numbers = []
elem = ''
alf = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4
}


def find_elem(elem):
    key = alf.get(elem[0])
    return alphabet[int(elem[1])][key]


for i in range(len(n)):
    if n[i] in '+-*':
        elem = n[i - 2] + n[i - 1]
        alf_arr_numbers.append(find_elem(elem))
    elif i == len(n) - 1:
        elem = n[i - 1] + n[i]
        alf_arr_numbers.append(find_elem(elem))

ans = f'{alf_arr_numbers[0]}'
for i in range(1, len(alf_arr_numbers)):
    ans += arr_znk[i - 1] + str(alf_arr_numbers[i])
print(eval(ans))
