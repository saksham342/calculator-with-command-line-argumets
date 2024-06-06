# calculator-with-command-line-argumets
 This Python script performs basic arithmetic operations (addition, subtraction, multiplication, and division) using command-line arguments.

This Python script performs basic arithmetic operations (addition, subtraction, multiplication, and division) using command-line arguments. To use the script, run it with three additional arguments: the first number (an integer), the second number (an integer), and a character representing the operation (a for addition, s for subtraction, m for multiplication, and d for division). For example, python3 calculator.py 12 4 a will output The result is: 16.

If the user provides incorrect input or the wrong number of arguments, the script will display an error message along with usage guidelines. Additionally, if the user requests help by passing -h or --help as an argument, the script will display a help message explaining the correct usage format and available operations. This ensures that users can easily understand how to use the script properly.

The script includes error handling to manage improper inputs, such as non-integer values for numbers or unrecognized characters for operations. This makes the script robust and user-friendly, guiding the user to provide the correct input format and ensuring that the script executes without crashing. Overall, this calculator script is a simple and efficient tool for performing basic arithmetic operations from the command line.
