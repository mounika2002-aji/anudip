#3Q.write a python programe that opens a file and handles FileNotFoundError exception if the file does not exist.

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Example usage
filename = "non_existent_file.txt"
open_file(filename)
