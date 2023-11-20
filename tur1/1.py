from math import ceil

shsjlichok_chicken = int(input())
shsjlichok_beef = int(input())
x = int(input())
chicken = ceil(shsjlichok_chicken / 4)
beef = ceil(shsjlichok_beef / 4)
x -= 2 * chicken
x -= 2 * beef
if x >= 0:
    print(1)
else:
    print(0)
