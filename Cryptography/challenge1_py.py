# NXR8 solution as a python script

def EshiftCipher(text, shift, showSteps):
    shift = shift % 26
    cipherText = ""
    if showSteps:
        print("Shift Cipher Encrypt: ", text)
        print("Formula: P + K mod 26 = C,Formula as code: chr((ord(char) - ord('a') + shift) % 26 + ord('a'))")
        print("Shift: ", shift)
    for char in text:
        if char.isalpha():
            if char.islower():
                if showSteps:
                    print("Char: ", char, "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
                cipherText += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                if showSteps:
                    print("Char: ", char, "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                cipherText += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipherText += char
    return cipherText

def DshiftCipher(text, shift, showSteps):
    shift = shift % 26
    cipherText = ""
    if showSteps:
        print("Shift Cipher Decrypt: ", text)
        print("Formula: C - K mod 26 = P,Formula as code: chr((ord(char) - ord('a') - shift) % 26 + ord('a'))")
        print("Shift: ", shift)
    for char in text:
        if char.isalpha():
            if char.islower():
                if showSteps:
                    print("Char: ", char, "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
                cipherText += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                if showSteps:
                    print("Char: ", char, "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                cipherText += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            cipherText += char
    return cipherText

def EvigenerCipher(text, key, showSteps):
    key = key.lower()
    cipherText = ""
    if showSteps:
        print("Vigener Cipher Encrypt: ", text)
        print("Formula: P + K mod 26 = C,Formula as code: chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))")
        print("Key: ", key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            if text[i].islower():
                if showSteps:
                    print("Char: ", text[i], "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a')))
                cipherText += chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))
            else:
                if showSteps:
                    print("Char: ", text[i], "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A')))
                cipherText += chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
        else:
            cipherText += text[i]
    return cipherText

def DvigenerCipher(text, key, showSteps):
    key = key.lower()
    cipherText = ""
    if showSteps:
        print("Vigener Cipher Decrypt: ", text)
        print("Formula: C - K mod 26 = P,Formula as code: chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))")
        print("Key: ", key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i % len(key)]) - ord('a')
            if text[i].islower():
                if showSteps:
                    print("Char: ", text[i], "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a')))
                cipherText += chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))
            else:
                if showSteps:
                    print("Char: ", text[i], "Shift: ", f"{shift:02}", "Cipher: ", chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A')))
                cipherText += chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A'))
        else:
            cipherText += text[i]
    return cipherText

if __name__ == "__main__":
    plainText = "CybersecurityandComputerScience"
    key = "apple"
    print("Plain Text: ", plainText)
    print("Key: ", key, "\n")

    print("output: ", EshiftCipher(plainText, 3, True), "\n")
    print("output: ", DshiftCipher(EshiftCipher(plainText, 3, False), 3, True), "\n")
    print("output: ", EvigenerCipher(plainText, key, True), "\n")
    print("output: ", DvigenerCipher(EvigenerCipher(plainText, key, False), key, True), "\n")

    print("=" * 50)

    print("Task1 Encrypt: ", EshiftCipher(plainText, 3, False))
    # print("Task1 Decrypt: ", DshiftCipher(EshiftCipher(plainText, 3, False), 3, False))
    print("Task1 Decrypt: ", plainText)

    print("Task2 Encrypt: ", EvigenerCipher(plainText, key, False))
    # print("Task2 Decrypt: ", DvigenerCipher(EvigenerCipher(plainText, key, False), key, False))
    print("Task2 Decrypt: ", plainText)
    

