# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    temp_list = names.readlines()
name_list = []
for name in temp_list:
    name = name.strip("\n")
    name_list.append(name)
with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    content = starting_letter.read()
    for invite_names in name_list:
        with open(f"Output/ReadyToSend/{invite_names}.txt", mode='w') as creating_letter:
            letters = content.replace("[name]", f"{invite_names}")
            creating_letter.write(letters)
