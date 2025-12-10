# from .utils import build_messege
from .utils import build_messege

class Validate_bin:
    @staticmethod
    def binary_length(bin:str) -> tuple[bool, str | None ]:
        """
            Docstring for binary_length
            
            :param bin: Description
            :type bin: str
            :return: Description
            :rtype: tuple[bool, str | None]
        """
        if len(bin)!= 10:
            return False, "The length of the binary number is incorrect (should contain 10 digits)"
        else:
            return True, None
        
    @staticmethod
    def dhe_typs_is_zeros_or_ones(bin:str) -> tuple[bool, str | None ]:
        for i in bin:
            if i not in ['1', '0']:
                return False, " The binary number does not currently contain only zeros and ones, which is an error"
        return True, None
    

    @staticmethod 
    def is_a_correct_sequence(bin:str) -> tuple[bool, str | None ]:
        fleg = 1
        for i in bin:
            if int(i) != fleg:
                fleg -= 1
        if fleg == 0:
            return True,None
        else:
            return False,  "The sequence is incorrect (a series of ones and then zeros)"
        

    @staticmethod
    def validation(bin_value) -> tuple[bool, str | None ]:
        isvalidate= False
        messege = None

        is_binary_length_validate, messege1 = Validate_bin.binary_length(bin_value)
        is_dhe_typs_is_zeros_or_ones_validate, messege2 = Validate_bin.dhe_typs_is_zeros_or_ones(bin_value)
        is_is_a_correct_sequence_validate, messege3 = Validate_bin.is_a_correct_sequence(bin_value)
        
        if (is_binary_length_validate and
            is_dhe_typs_is_zeros_or_ones_validate and
            is_is_a_correct_sequence_validate):
            isvalidate = True
        else:
            messege = build_messege(messege1, messege2, messege3)
            
        return isvalidate, messege
    

class Validate_dec:
    @staticmethod
    def is_within_range(dec : str) -> tuple[bool, str|None]:
        if int(dec) < 0 or int(dec) > 1024:
            return False, 'The decimal number is out of range (1024-0)'
        else:
            return True ,None
        
    @staticmethod
    def validation(bin_value )->tuple[bool, str |None ]:
        is_is_within_range, massege_WID = Validate_dec.is_within_range(bin_value)

        isvalidate = is_is_within_range
        messege = massege_WID
        if is_is_within_range:
            isvalidate= True
            return isvalidate, messege
        
        return isvalidate, messege


