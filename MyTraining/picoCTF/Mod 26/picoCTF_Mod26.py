# NXR8 solution as a python script

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


if __name__ == "__main__":
    plainText = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
    print("Plain Text: ", plainText)

    print("output: ", DshiftCipher(plainText, 13, True), "\n")

    

