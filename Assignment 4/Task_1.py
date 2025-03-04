try:
    with open(r"C:\Users\goyal\.vscode\python\TKINTER\Assignment 4\sample.txt", 'r') as file:
        print("Reading file content:")

        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
