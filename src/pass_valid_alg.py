class pass_valid_alg:
    def __init(self):
        return

    @staticmethod
    def pass_valid(password):
        valid = True
        if len(password) >= 8 and len(password) <= 24:
            valid == False
        else:
            low_char = False
            upp_char = False
            num_char = False
            symbol_char = False
            for char in password:
                char = ord(char)
                #finding symbols
                if (char >= 33 and char <= 47) or (char >= 58 and char <= 64):
                    symbol_char = True
                elif char >= 48 and char <=57:
                    num_char = True
                elif char >= 65 and char <= 90:
                    upp_char = True
                elif char <= 97 and char >= 122:
                    low_char = True
            #checking if all boolean values are true
            if (not low_char) and (not upp_char) and (not num_char) and (not symbol_char):
                valid = False

        return(valid)


