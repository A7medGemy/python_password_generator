import string
import random

while True:
    try:
        passwordLength = int(input("Enter the length of the password : "))
        if passwordLength <= 0:
            print("Length must be greater than zero")
            continue
        break
    except ValueError:
        print("Please enter a valid number")

upperCaseValidation = input("Would you like the password includes uppercase letters , press Y or N : ").upper()
digitsValidation = input("Would you like the password includes digits , press Y or N : ").upper()
symbolsValidation = input("Would you like the password includes symbols , press Y or N :").upper()

upperCaseLetters = string.ascii_uppercase
lowerCaseLetters = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

password = lowerCaseLetters
if upperCaseValidation == "Y":
    password += upperCaseLetters
if digitsValidation == "Y":
    password += digits
if symbolsValidation == "Y":
    password += symbols

print("\nGenerated password:")
generatedPassword = "".join(random.choices(password,k=passwordLength))
print(generatedPassword)


# except ValueError:
#     print("Enter just a y or n letter")
