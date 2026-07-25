#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# import os
# print(os.getcwd())

PLACE_HOLDER="[name]"

with open("/001. PYTHON/Vpython learning/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    letter=file.read()
    print(letter)
with open("/001. PYTHON/Vpython learning/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    names_files=name_file.readlines()
    print(names_files) 

for n in names_files:
    stripped=n.strip()
    new_letter=letter.replace(PLACE_HOLDER,stripped)
    print(new_letter)
    with open(f"/001. PYTHON/Vpython learning/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped}.docx",mode="w") as completed:
        completed.write(new_letter)