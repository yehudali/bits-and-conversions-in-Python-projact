from src.validate import Validate_bin, Validate_dec
from src.utils import build_messege
from src.Conversions import *


def user_input():
    '''
    Docstring for user_input
    
        Accept input from the user-in-whail loop, perform data validation,
        print error messages if invalid
    '''

    while True:
        bin_value = input('Binara sequence: ')
        decimal_value = input('decimal num: ')

        isvalidate_bin, messege_bin = Validate_bin.validation(bin_value)
        isvalidate_dec, messege_dec = Validate_dec.validation(decimal_value)

        messege = build_messege(messege_bin, messege_dec)

        if isvalidate_bin and isvalidate_dec:
            return bin_value, decimal_value
        else:
            print(messege)



def main():
    bin_value, decimal_value = user_input()
    decimal_input_in_binarybinary = dec_to_bin(int(decimal_value))
    left_part, right_part = split_by_mask(bin_value, decimal_input_in_binarybinary)
    result_in_decimal : list[int] = [bin_to_dec(left_part),bin_to_dec(right_part)]

    print('Binary Mask Input: ',bin_value)
    print('Decimal Input: ', decimal_value)

    print('Input in Binary: ',decimal_input_in_binarybinary)
    
    print('Left Part (Binary): ', left_part)
    print('`right Part (Binary):` ', right_part)

    print('Result in Decimal: ', result_in_decimal)

    with open('bit_mask_result_[name yehuda linker].txt', 'a')as myfile:
        myfile.write(f"\n")
        myfile.write(f"Binary Mask Input: {bin_value} \n")
        myfile.write(f"Decimal Input: {decimal_value} \n")
        myfile.write(f"Input in Binary: {decimal_input_in_binarybinary}\n")
        myfile.write(f"Left Part (Binary): {left_part}\n")
        myfile.write(f"right Part (Binary): {right_part}\n")
        myfile.write(f"Result in Decimal:{result_in_decimal}\n")
        myfile.write(f"\n")
        print("Writing to file was successful.")
    
if __name__ == "__main__":
    main()
    



# Binary Mask Input: 1111000000 
# Decimal Input: 512 
# Input in Binary: 1000000000
# Left Part (Binary): 1000
# right Part (Binary): 000000
# Result in Decimal:[8, 0]
