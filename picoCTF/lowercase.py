user_input = input("Enter a word: ")
user_input = user_input.lower().replace(" ", "_")
print("picoCTF{",user_input,"}",sep="")