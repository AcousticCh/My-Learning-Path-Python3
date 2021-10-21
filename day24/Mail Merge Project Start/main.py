#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_setup = str(letter.read())
    with open("./Input/Names/invited_names.txt", "r") as names:
        for n in names.readlines():
            with open(f"./Output/ReadyToSend/letter_to_{n}.txt", "w") as new_letter:
                
                new = letter_setup.replace("[name]", n.strip())
                new_letter.write(new)
            
            
