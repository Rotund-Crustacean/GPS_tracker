class hashAlg:
    def __init__(self):
        return

    @staticmethod
    def __make_ascii_string__(input):
        #casting input as integer
        input = str(input)
        output = ''

        #iterating through characters in input
        for char in input:
            #concatenating character ascii values
            output += str(ord(char))
        return output

    @staticmethod
    def hash(plain_pass, plain_user):
        #declaring variables
        ciphertext = ''
        salt_value = ''

        #converting password into ciphertext
        ciphertext = hashAlg.__make_ascii_string__(plain_pass)
        ciphertext = int(ciphertext)

        #converting username into salt
        salt_value = hashAlg.__make_ascii_string__(plain_user)
        salt_value = int(salt_value)

        #should produce a deterministic but not reversible output
        ciphertext = ciphertext * salt_value
        #4374 is a prime number
        ciphertext = ciphertext % 4373
        #casts ciphertext back to a string
        ciphertext = str(ciphertext)
        ciphertext = ciphertext[10]
        return ciphertext
