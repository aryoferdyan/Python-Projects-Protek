shift = 5 # defining the shift count

text = "SAYA CINTA PYTHON"

encryption = ""

for i in text:

    if i.isupper():
        i_unicode = ord(i)
        i_index = ord(i) - ord("A")

        # perform the shift
        new_index = (i_index + shift) % 26

        # convert to new character
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # append to encrypted string
        encryption = encryption + new_character

    else:

        # since character is not uppercase, leave it as it is
        encryption += i
        
print("Plain text:",text)

print("Encrypted text:",encryption)