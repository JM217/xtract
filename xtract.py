#!/usr/bin/env python
#extract text from a text file and output the lines containing that text to a new file
#easily clean up files by removing unwanted strings
#v0.2
#Author - JM217
def select_file():
    while True:
        file_path = input("Enter the path to the file you want to read: ")
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")


def extract_lines(lines, search_string):
    return [line for line in lines if search_string in line]


def remove_characters(lines, characters_to_remove):
    return [line.replace(characters_to_remove, "") for line in lines]


def write_to_file(lines, output_file):
    with open(output_file, 'w') as file:
        file.writelines(lines)


def main():
    print("Select File:")
    lines = select_file()

    action = input("Enter the action you want to perform:\n"
                   "1. Extract lines containing a specific string and write to a new file.\n"
                   "2. Remove characters from the file and write to a new file.\n")

    if action == "1":
        search_string = input("Enter the string you want to search for: ")
        filtered_lines = extract_lines(lines, search_string)
        output_file = input("Enter the path for the output file with filtered lines: ")
        write_to_file(filtered_lines, output_file)
        print(f"Filtered lines containing '{search_string}' have been written to '{output_file}'.")
    elif action == "2":
        characters_to_remove = input("Enter the characters you want to remove from the original file: ")
        modified_lines = remove_characters(lines, characters_to_remove)
        output_file = input("Enter the path for the output file with modified lines: ")
        write_to_file(modified_lines, output_file)
        print(f"Modified file with characters removed has been written to '{output_file}'.")
    else:
        print("Invalid option. Please enter either '1' or '2'.")


if __name__ == "__main__":
    main()
