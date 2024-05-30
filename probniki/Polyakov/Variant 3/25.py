def f(star, q1, ans):
    global c
    s = "3{}1{}57"
    num = int(s.format(star, q1))
    if num % c == 0:
        ans.append(num)


c = 2023
max_star_len = 2
ans = []
for q1 in range(100):
    f("", q1, ans)
    for star in range(10 ** max_star_len):
        star_str = str(star)
        for i in range(len(star_str), max_star_len + 1):
            f(star_str, q1, ans)
            star_str = "0" + star_str
ans.sort()
for num in ans:
    print(num, num // c)
