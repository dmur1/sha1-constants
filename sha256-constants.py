import math

# both sha-256 and BLAKE-256 use these constants

IV0 = 0x6a09e667
IV1 = 0xbb67ae85
IV2 = 0x3c6ef372
IV3 = 0xa54ff53a
IV4 = 0x510e527f
IV5 = 0x9b05688c
IV6 = 0x1f83d9ab
IV7 = 0x5be0cd19

IV = [IV0, IV1, IV2, IV3, IV4, IV5, IV6, IV7]
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

for index in range(0, len(IV)):
    iv = IV[index]
    prime = PRIMES[index]
    print(f"IV{index}: {iv:08x}")
    sqrt_prime = math.sqrt(prime)
    print(f" int((math.sqrt({prime}) % 1) * (2 ** 32)) => {int((sqrt_prime % 1) * (2 ** 32)):08x}")
