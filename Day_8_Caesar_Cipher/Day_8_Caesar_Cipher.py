import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(plain_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for i in plain_text:
        if i in alphabet: 
            text_index=alphabet.index(i)
            text_index+=shift_amount
            end_text+=alphabet[text_index]
        else:
            end_text+=i
    print(f"The {cipher_direction}d text is {end_text}.")
choice="yes"
while choice!="no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift%=26
    caesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

