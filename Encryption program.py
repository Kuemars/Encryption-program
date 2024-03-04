import random
import string

enc_char = " " + string.punctuation + string.digits + string.ascii_letters
enc_char = list(enc_char)
keys = enc_char.copy()
random.shuffle(keys)

while True:
    QQ = input("Do you want to encrypt your message? ")
    if QQ.upper() == "NO":
        break
    else:
        initial_text = input("Enter the message you want to encrypt: ")
        encrypted_text = ""

        for letter in initial_text:
            index = enc_char.index(letter)
            encrypted_text += keys[index]

        print(f"encrypted message: {encrypted_text}")
        question = input("Do you want to decrypt the message? Type Yes or No: ")
        if question.upper() == "YES":
            encrypted_text = input("Enter the message you want to decrypt: ")
            initial_text = ""

            for letter in encrypted_text:
                index = keys.index(letter)
                initial_text += enc_char[index]

            print(f"Decrypted message: {initial_text}")
            AA = input("Do you want to continue? ")
            if AA.upper() == "NO":
                break
            else:
                continue

        else:
            print("Your message and it's encryption will be deleted "
                  "after you close the program.")
            open_close = input("Do you want to continue? ")
            if open_close.upper() == "NO":
                break
            else:
                continue
        continue