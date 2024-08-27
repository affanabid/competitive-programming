def significant_bits(n):
    count = 0
    while n > 0:
        n = n // 2
        count += 1
    return count

def sig(n):
    return n.bit_length()

n = 5
print(sig(n) == significant_bits(n))