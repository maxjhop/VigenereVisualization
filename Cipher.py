""" Dictionary with indices as keys and letters of the alphabet as values. This will be used by the encryption function
    in order to find the encrypted letter by its index. For example, if the encryption function determines that the encrypted
    letter is at index 22, then index2alpha[22] will return 'w'
"""
index2alpha = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j",
                10:"k", 11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s",
                19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"
                }

""" Dictionary with each letter of the alphabet as a key and an index as a value. This will be used by the encryption
    function to add together the indices of the letters in the plaintext string and keyword string in order to find the
    correct index of the encrypted letter. For example: If the current plaintext letter is 'b', and the current keyword
    letter is 'k', then the encrypted letter index will be: 1 + 10 = 11
"""
alpha2index = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9,
                "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18,
                "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25
                }

# ===================================================================================================================================================================
# ==================================================================== Encryption Function ==========================================================================

def Encrypt(plainText, Keyword):
    keyword = Keyword.replace(" ", "").lower() # Remove any spaces and uppercase letters from the keyword

    # Error Handling. Make sure the keyword is not an empty string
    if (len(keyword) == 0):
        print("ERROR! Keyword cannot be null")
        return None
    
    # Error Handling. Check to make sure the keyword only has letters
    if (not keyword.isalpha()):
        print("ERROR! Keyword <{}> must only contain letters".format(keyword))
        return None

    # This variable represents the current index into the keyword string
    keywordIndex = 0

    inst = []
    
    # 'length' is the length of the keyword. Since the plaintext is most likely going to be longer than
    # the keyword, this length variable is used to calculate an appropriate index into the keyword string
    # via remainder (modulo) division. 
    length = len(keyword)

    # retStr is a string that will contain the encrypted text after the encryption process has finished
    retStr = ''
    
    for letter in plainText: # Iterate through each letter in the plainText message

        char = "" # This will hold the encrypted character to be added to the return string
        
        if (letter != " " and letter.isalpha()): # If the current letter is not a space

            # The following line calculates the index of the encrypted letter in the alphabet. It does this by adding
            # together the indices of the plaintext letter and keyword letter in the alphabet.
            ind1 = alpha2index[letter.lower()]
            ind2 = alpha2index[keyword[keywordIndex]]
            encryptLetterIndex = (alpha2index[letter.lower()] + alpha2index[keyword[keywordIndex]]) % 26

            inst.append((ind1, ind2, encryptLetterIndex))

            # This uses the previously calculated index to find the encrypted letter in the alphabet
            char = index2alpha[encryptLetterIndex]

            # If the plaintext letter is uppercase, then the encrypted letter will also be upper case. 
            if (letter.isupper()):
                char = char.upper() # Set the encrypted character to an upper case version of itself
                
            # Increment the keyword index to simulate a 'repeating' keyword
            keywordIndex = (keywordIndex + 1) % length
            
        else: # If the current letter is not a letter of the alphabet
            char = letter # Add whatever character it is to the encrypted string

        retStr = retStr + char # Add the character to the return string
    #return result, list of indices, original plaintext, and original keyword
    return (retStr, inst, plainText, Keyword)

# ===================================================================================================================================================================
# ==================================================================== Decryption Function ==========================================================================

def Decrypt(cipherText, Keyword):
    keyword = Keyword.replace(" ", "").lower() # Remove any spaces and uppercase letters from the keyword
    
    # Error Handling. Make sure the keyword is not an empty string
    if (len(keyword) == 0):
        print("ERROR! Keyword cannot be null")
        return None

    # Error Handling. Check to make sure the keyword only has letters
    if (not keyword.isalpha()):
        print("ERROR! Keyword <{}> must only contain letters".format(keyword))
        return None

    # This variable represents the current index into the keyword string
    keywordIndex = 0
    # Length of the keyword. Since the ciphertext is most likely going to be longer than
    # the keyword, this length variable is used to calculate an appropriate index into the keyword string
    # via remainder (modulo) division.
    keywordLength = len(keyword)

    inst = []
    
    # retStr is a string that will contain the decrypted text after the decryption process has finished
    retStr = ""
    
    for letter in cipherText: # Iterate through each letter in the plainText message

        char = "" # This will hold the decrypted character to be added to the return string

        if (letter != " " and letter.isalpha()): # If the current letter is not a space

            # The following line calculates the index of the decrypted letter in the alphabet. It does this by subtracting
            # the indices of the ciphertext letter and keyword letter from each other
            ind1 = alpha2index[letter.lower()]
            ind2 = alpha2index[keyword[keywordIndex]]
            decryptLetterIndex = (alpha2index[letter.lower()] - alpha2index[keyword[keywordIndex]]) % 26

            inst.append((decryptLetterIndex, ind2, decryptLetterIndex))
            
            # This uses the previously calculated index to find the encrypted letter in the alphabet
            char = index2alpha[decryptLetterIndex]

            # If the plaintext letter is uppercase, then the encrypted letter will also be upper case. 
            if (letter.isupper()):
                char = char.upper() # The charater to be added to the result string is a space

            # Increment the keyword index to simulate a 'repeating' keyword
            keywordIndex = (keywordIndex + 1) % keywordLength
            
        else: # If the current letter is not a letter of the alphabet
            char = letter # Add whatever character it is to the decrypted string

        retStr = retStr + char # Add the character to the return string
    #return result, list of indices, original cipher text, and original keyword
    return (retStr, inst, cipherText, Keyword)
