def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (converting to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print("Error: There was an issue reading or writing the file.")


def read_file_with_error_handling():
    filename = input("Please enter the filename: ")
    
    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Unable to read the file '{filename}'.")


# --- Main Code ---
input_filename = "jean.txt"  
output_filename = "aush.txt"  

# Read and write operation
read_and_write_file(input_filename, output_filename)

# Error handling for reading a file
read_file_with_error_handling()
