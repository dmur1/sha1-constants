import math

# these are the initial values for SHA-1
# we can see that they are byte swapped contiguous sequences with the exception
# of E which can be thought of as two interleaved sequences
# these values have a hamming weight of 0.5 due to having an equal number of 1s and 0s
A = 0x67452301 # 0x01234567
B = 0xEFCDAB89 # 0x89abcdef
C = 0x98BADCFE # 0xfedcba98
D = 0x10325476 # 0x76543210
E = 0xC3D2E1F0 # 0xf0e1d2c3 ~ 0xfedc (+) 0x0123

INITIAL_VALUES = [A, B, C, D, E]

def reverse_byte_order(value):
    b0 = value & 0xff
    b1 = (value & 0xff00) >> 8
    b2 = (value & 0xff0000) >> 16
    b3 = (value & 0xff000000) >> 24
    return (b0 << 24) | (b1 << 16) | (b2 << 8) | b3

def count_num_bits_set(value):
    num_bits_set = 0
    for bit_index in range(0, 32):
        if (value & (1 << bit_index)) > 0:
            num_bits_set += 1
    return num_bits_set

print('initial values for SHA-1')

total_num_of_bits_set = 0
for index in range(0, len(INITIAL_VALUES)):
    initial_value = INITIAL_VALUES[index]
    initial_value_name = chr(ord('A') + index)
    print(f'{initial_value_name}: 0x{initial_value:08X}')
    print(f'  reversed byte order 0x{reverse_byte_order(initial_value):08X}')
    num_bits_set = count_num_bits_set(initial_value)
    total_num_of_bits_set += num_bits_set
    print(f'  num bits set {num_bits_set}')
    
print(f'total number of bits set: {total_num_of_bits_set} => {(total_num_of_bits_set / 160) * 100.0}% of bits are set')
print('\n')

# these are the stage constants for SHA-1
# each of of these is used for 20 of the 80 total rounds
# these numbers are computed by truncating the product of 2**30 and the square
# root of 2, 3, 5 and 10
K1 = 0x5A827999
K2 = 0x6ED9EBA1
K3 = 0x8F1BBCDC
K4 = 0xCA62C1D6

ROUND_CONSTANTS = [K1, K2, K3, K4]
NUMERICAL_BASIS = [2, 3, 5, 10]

print('round constants for SHA-1')

for index in range(0, len(ROUND_CONSTANTS)):
    round_constant = ROUND_CONSTANTS[index]
    round_constant_name = 'K' + chr((ord('1') + index))
    print(f"{round_constant_name}: 0x{round_constant:08X} {round_constant:08}")
    basis = NUMERICAL_BASIS[index]
    constant = math.sqrt(basis) * (2 ** 30)
    print(f'  (2 ** 30) * math.sqrt({basis}) => {constant}')
    print(f'  int((2 ** 30) * math.sqrt({basis})) => {int(constant)} => 0x{int(constant):08X}')

