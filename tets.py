import math
from scipy.special import gammaincc


def freq_bit_test(bits: str):
    sum = 0
    for i in bits:
        if i == 0:
            sum += -1
        else:
            sum += 1
    itog = math.erfc((sum / math.sqrt(128)) / math.sqrt(2))
    return itog


def ident_secutive_bits_test(bits):
    freq_1 = bits.count('1') / 128
    c_f = bits.count('0')
    runs = [bits[0]]
    for i in range(1, 128):
        if bits[i] != bits[i - 1]:
            runs.append(bits[i])

    num = len(runs)
    P = math.erfc(abs(num - 2 * 128 * freq_1 * (1 - freq_1)) / (2 * math.sqrt(2 * 128) * freq_1 * (1 - freq_1)))
    print(P)
    return P > 0.01


def test_longst_seq(bits):
    c_b = 128 // 8
    mas_count = []

    for i in range(c_b):
        block = bits[i * 8: (i + 1) * 8]
        one = 0
        max_one_in_block = 0
        max_run = 0
        for bit in block:
            if bit == '1':
                one += 1
                max_one_in_block = max(max_one_in_block, one)
            else:
                one = 0
        max_run = max(max_run, max_one_in_block)
        mas_count.append(max_run)

    v1 = sum(x <= 1 for x in mas_count)
    v2 = sum(x == 2 for x in mas_count)
    v3 = sum(x == 3 for x in mas_count)
    v4 = sum(x > 4 for x in mas_count)
    k0 = 0.2148
    k1 = 0.3672
    k2 = 0.2305
    k3 = 0.1875

    X = ((v1 - 16 * k0) ** 2) / (16 * k0) + ((v2 - 16 * k1) ** 2) / (16 * k1) + ((v3 - 16 * k2) ** 2) / (16 * k2) + (
            (v4 - 16 * k3) ** 2) / (16 * k3)
    P = gammaincc(3 / 2, X / 2)

    print(P)
    return (P > 0.01)


if __name__ == "__main__":
    text = str

    with open("gen_binary_text.txt", "r+") as file:
        text = file.readline()

    print("Бинарная последовательность: ")
    print(text)

    bits = list(text)

    print("Частотный побитовый тест: ")
    print(freq_bit_test(bits))

    print("Тест на одинаковые подряд идущие биты: ")
    print(ident_secutive_bits_test(bits))

    print("Тест на самую длинную последовательность единиц в блоке: ")
    print(test_longst_seq(bits))
