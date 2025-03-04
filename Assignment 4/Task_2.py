user_input = input("Enter data to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
    
additional_input = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")
