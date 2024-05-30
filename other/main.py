ipadr = '154.63.206.129'.split('.')
maska = '154.63.100.75'.split('.')
# maska = '255.255.128.0'.split('.')
ipadr = [int(s) for s in ipadr]
maska = [int(s) for s in maska]
# print(bin(200))
print(str(bin(maska[0] & ipadr[0]) + "." + bin(maska[1] & ipadr[1]) + '.' + bin(maska[2] & ipadr[2]) + '.' + bin(
    maska[3] & ipadr[3])).replace("0b", ""))
print([bin(s).replace('0b', '') for s in ipadr])
print([bin(s).replace('0b', '') for s in maska])
print(2 ** 15)
