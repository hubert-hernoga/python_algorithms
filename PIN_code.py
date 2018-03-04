# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.


def validate_pin(pin):
    if pin.isdigit():
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False


def validate_pin1(pin):
    return len(pin) in (4, 6) and pin.isdigit()


"should return False for pins with length other than 4 or 6"
print(validate_pin("1"))
print(validate_pin("12"))
print(validate_pin("123"))
print(validate_pin("12345"))
print(validate_pin("1234567"))
print(validate_pin("-1234"))
print(validate_pin("1.234"))
print(validate_pin("00000000"))
print('--------------------')
"should return False for pins which contain characters other than digits"
print(validate_pin("a234"))
print(validate_pin(".234"))
print('--------------------')
"should return True for valid pins"
print(validate_pin("1234"))
print(validate_pin("0000"))
print(validate_pin("1111"))
print(validate_pin("123456"))
print(validate_pin("098765"))
print(validate_pin("000000"))
print(validate_pin("123456"))
print(validate_pin("090909"))
print('-------------------------')
"should return False for pins with length other than 4 or 6"
print(validate_pin1("1"))
print(validate_pin1("12"))
print(validate_pin1("123"))
print(validate_pin1("12345"))
print(validate_pin1("1234567"))
print(validate_pin1("-1234"))
print(validate_pin1("1.234"))
print(validate_pin1("00000000"))
print('--------------------')
"should return False for pins which contain characters other than digits"
print(validate_pin1("a234"))
print(validate_pin1(".234"))
print('--------------------')
"should return True for valid pins"
print(validate_pin1("1234"))
print(validate_pin1("0000"))
print(validate_pin1("1111"))
print(validate_pin1("123456"))
print(validate_pin1("098765"))
print(validate_pin1("000000"))
print(validate_pin1("123456"))
print(validate_pin1("090909"))