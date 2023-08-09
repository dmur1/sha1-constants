K1 = 1518500251
K2 = 0x6ED9EBA1
K3 = 0x8F1BBCDD
K4 = 0xCA62C1D7

ROUND_CONSTANTS = [K1, K2, K3, K4]

def count_num_bits_set(value):
    num_bits_set = 0
    for bit_index in range(0, 32):
        if (value & (1 << bit_index)) > 0:
            num_bits_set += 1
    return num_bits_set

print('alt round constants for SHA-1')

total_num_of_bits_set = 0
for index in range(0, len(ROUND_CONSTANTS)):
    round_constant = ROUND_CONSTANTS[index]
    round_constant_name = 'K' + chr((ord('1') + index))
    print(f"{round_constant_name}: 0x{round_constant:08X} {round_constant:08}")
    num_bits_set = count_num_bits_set(round_constant)
    total_num_of_bits_set += num_bits_set
    print(f'  num bits set {num_bits_set}')
    
print(f'total number of bits set: {total_num_of_bits_set} => {(total_num_of_bits_set / (4*32)) * 100.0}% of bits are set')
print('\n')
