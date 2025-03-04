                                Task 1

File Reading Example

Description

This Python script reads the contents of a specified text file and prints each line with its corresponding line number. It also handles file not found errors gracefully.

How It Works

The script attempts to open the file sample.txt from the specified path.
It reads and prints each line from the file, prepending the line number.
If the file does not exist, an error message is displayed.

Usage

Ensure that sample.txt exists in the specified directory.
Run the script in a Python environment.
If the file exists, the script prints its contents line by line.
If the file is missing, an error message is shown.

Example Output

Reading file content:
Line 1: This is the first line.
Line 2: This is the second line.
...

If the file is missing:
Error: The file 'sample.txt' was not found.

Requirements

Python 3.x

A valid text file (sample.txt) in the specified directory.

Notes

The script uses exception handling (try-except) to manage errors.
Modify the file path to match your system's directory structure.

License

This project is open-source and available for modification and distribution.


                              Task 2

File Write and Append Example

Description

This Python script demonstrates how to write user input to a file, append additional input, and read the final content of the file.

How It Works

The script prompts the user to enter data, which is written to output.txt.
It then asks for additional input and appends it to the same file.
Finally, it reads and displays the contents of output.txt, showing each line with its corresponding line number.

Usage

Run the script in a Python environment.

Enter data when prompted; this will be written to output.txt.
Enter additional data when prompted; this will be appended to the file.
The script will display the final content of output.txt.

Example Output

Enter data to write to the file: Hello, world!
Enter additional data to append: This is a test.

Final content of output.txt:
Line 1: Hello, world!
Line 2: This is a test.

Requirements

Python 3.x

Notes

The script uses the w mode to write data, which overwrites existing content.
The a mode is used to append data without erasing previous content.
The file output.txt is created if it does not already exist.

License

This project is open-source and available for modification and distribution.

