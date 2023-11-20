from math import gcd, lcm
from fractions import Fraction as f


def cutting_fract(numer, denom):
    d = gcd(numer, denom)
    return numer // d, denom // d


def common_denom(fract1, fract2):
    new_denom = lcm(fract1[1], fract2[2])
    return [fract1[0] * (new_denom // fract1[1]), new_denom], [fract2[0] * (new_denom // fract2[1]), new_denom]


# 1 4/5 + 3 2/21

s = input().split(' ')
nums, znak = [[0, 0, 1], [0, 0, 1]], ''
index = 0  # index of number in nums

# как отличать num1 и num2? Переход от одного к другому происходит тогда, когда считываем знак операции
# варианты: проверять, считан ли знак, использовать определенный флаг-индекс, чтобы уменьшить количество if

# 7 -> [7, 1]
# 1/5 -> [1, 5]
# 3 3/4 -> [15, 4]
# [1, 4, 5] [0, 11, 49]
# elem является одним из:
# целое число
# дробь (целое число/целое число)
# знак операции (+-)
# ответ в формате: целое число целое число/целое число
for elem in s:
    # находим дробь или целое число, или знак и записываю числитель и знаменатель в 1 и 2 элемента массива, иначе записываем целое число в 0 элемент
    # определяем тип элемента elem: дробь или целое число, или знак
    # если дробь, то разделяем на числитель и знаменатель
    if '/' in elem:
        # nums[index][1:3] = map(int, elem.split("/"))
        numerator, denominator = map(int, elem.split("/"))
        nums[index][1] = numerator
        nums[index][2] = denominator
    # если знак
    elif elem in "+-":
        znak = elem
        index += 1
    # если целое число, 
    else:
        nums[index][0] = int(elem)
ans = [0, 0, 0]
if znak == '+':
    ans[0] = nums[0][0] + nums[1][0]
    ans[1] = f(nums[0][1], nums[0][2]) + f(nums[1][1], nums[1][2])
    ans[2] = ans[1].denominator
    ans[1] = ans[1].numerator
if znak == '-':
    ans[0] = nums[0][0] - nums[1][0]
    ans[1] = f(nums[0][1], nums[0][2]) - f(nums[1][1], nums[1][2])
    ans[2] = ans[1].denominator
    ans[1] = ans[1].numerator
print(ans)
# if len(ans) > 1:
#     ans[0] += ans[1] // ans[2]
#     ans[1] -= ans[2] * (ans[1] // ans[2])
#     if ans[1] != 0:
#         ans[1], ans[2] = cutting_fract(ans[1], ans[2])
#         print(f'{ans[0]} {ans[1]}/{ans[2]}')
#     else:
#         print(ans[0])
# else:
#     print(ans[0])

# как отличать операции (просто)
# как складывать или вычитать дроби
# упрощение дроби, сокращение числ и знаменатель
# приведение к общему знаменателю
# операция
# учет целой и дробной части
