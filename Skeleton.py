def  InputPlainText():
    plainText = input("Please enter the plaintext: ")
    return plainText

def InputCypherText():
    cypherText = input("Please enter the cypher text: ")
    return cypherText

def InputKey():
    key = int(input("Please enter the key value: "))
    return key

def Encrypt(PlainText, Key ):
    CharPos = 0
    CipherText = ""
    Character = ""
    CharacterCode = ""

    for CharPos in range (len(PlainText)):
        Character = PlainText[CharPos]
        CharacterCode = ord(Character)
        if Character >= "A" and Character <= "Z":
            CharacterCode = CharacterCode + Key
            if CharacterCode > ord("Z"):
                CharacterCode = CharacterCode - 26
        CipherText = CipherText + chr(CharacterCode)

    return CipherText

def Decrypt(CypherText, Key ):
    CharPos = 0
    PlainText = ""
    Character = ""
    CharacterCode = 0

    for CharPos in range( len(CypherText)):
        Character = CypherText[CharPos]
        CharacterCode = ord(Character)
        if CharacterCode >= ord("A") and CharacterCode <= ord("Z"):
            CharacterCode = CharacterCode - Key
            if CharacterCode < ord("A"):
                CharacterCode = CharacterCode + 26
        PlainText = PlainText + chr(CharacterCode)

    return PlainText

def LoadPlainText():
        PlainText = ""
        return PlainText


def displayMenu():
    print("K Input Key")
    print("P Input Plaintext")
    print("C Input Ciphertext")
    print("L Load Plaintext")
    print("E Encrypt Plaintext")
    print("D Decrypt Ciphertext")
    print("Q Quit")


if __name__ == "__main__":
    menuOption = ""
    key = 3
    plainText = ""
    cypherText = ""

    while menuOption != "Q":
        displayMenu()
        menuOption = input("Enter Option > ").upper()
        if menuOption == "K":
            Key = int(input())
        elif menuOption == "P":
            plainText = InputPlainText()
            print("PlainText is : ", plainText)
        elif menuOption == "C":
            cypherText = InputCypherText()
        elif menuOption == "L":
            PlainText = LoadPlainText()
        elif menuOption == "E":
            print("Encrypting ", plainText)
            cypherText = Encrypt(plainText, key)
            print ("Cypher Text is : ", cypherText)
        elif menuOption == "D":
            plainText = Decrypt(cypherText, key)
            print ("Plain Text is : ", plainText )






