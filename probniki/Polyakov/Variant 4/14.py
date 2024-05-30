from other.defines import conv
import sys

sys.set_int_max_str_digits(10000)
s = 7 * 512 ** 3200 + 6 * 256 ** 3100 - 5 * 64 ** 3000 - 4 * 8 ** 2900 - 1542
s = conv(str(s), 10, 64)
print(s.count('0'))
