from math import ceil

for i in range(ceil(289_123_456 ** 0.25), int(389_123_456 ** 0.25) + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if not i % j:  # Проверка на простое число
            break
    else:
        print(i ** 4, i ** 3)
