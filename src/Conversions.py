

def dec_to_bin(decimal:int)-> str:
    binary = ""

    if decimal == 0:
        binary = "0"
    else:
        while decimal > 0:
            remainder = decimal % 2  # Get the remainder which is the last binary digit (0 or 1)
            binary = str(remainder) + binary  # Add it to the front of the result
            decimal = decimal // 2  # Divide number by 2 (integer division)
    return binary


def bin_to_dec(bin:str)->int:
    binary = bin
    decimal = 0
    power = 0

    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    # print(f"Decimal value is {decimal}")

    return decimal

def bin_to_dec2(bin:str)-> int:
    dec = int(bin, 2)
    return dec


def split_by_mask(masc:str, dec_in_bin: str)->tuple[str, str]:
    sum_1s=0
    for num in masc:
        if num == '1':
            sum_1s += 1
    left_part = dec_in_bin[:sum_1s]
    right_part = dec_in_bin[sum_1s:]

    return left_part, right_part