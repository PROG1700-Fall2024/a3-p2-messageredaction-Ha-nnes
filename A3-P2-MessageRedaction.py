#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0474277     
#Student Name: Hannes Meyer-Rahlfs  

def remove_letters(sentence, letters_to_remove): 
    
    modified_sentence = "" #creating empty string
    removed_count = 0      #creating empty counter for # of letter to remove

    # Looping through each character in the input sentence
    for char in sentence:
        if char.lower() in letters_to_remove: #checking if the character (changed to lowercase) is in the list
            modified_sentence += "_" #this is to replace the character with an underscore
            removed_count += 1 #simple counter for the removed letters
        else:
            modified_sentence += char

    return modified_sentence, removed_count #return statement to send values back

#prompting input and seeing if user wants to exit as this is an infinite loop
def main():
    print("Welcome to the Letter Removal Program!") #welcome message so user knows what the application is
    
    while True: 
        sentence = input("\nType a phrase (or quit to exit program): ").strip() 

        #if statement so if they type quit the program will exit 
        if sentence.lower() == "quit": 
            print("Goodbye!")
            break
        
        letters = input("Type a comma-separated list of letters to redact: ").strip() # getting list of letters to redact from user
        letters_to_remove = [letter.strip().lower() for letter in letters.split(",")] # converting the input to a list of lowercase letters, I used .split to get rid of commas and .strip to remove spaces.
        modified_sentence, removed_count = remove_letters(sentence, letters_to_remove)# calling remove_letters function

        #Displayign results
        print(f"Number of letters redacted: {removed_count}")
        print(f"Redacted phrase: {modified_sentence}")

main()
