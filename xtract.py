#!/usr/bin/env python
#extract text from a text file and output the lines containing that text to a new file
#v0.1
def select_file():
    while True:
        file_path = input("File path to read: ")
        try:
            with open(file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")


def specify_string():
    return input("String to search for: ")


def extract_lines(lines, search_string):
    return [line for line in lines if search_string in line]


def write_to_file(lines, output_file):
    with open(output_file, 'w') as file:
        file.writelines(lines)


def main():
    print("Select File:")
    lines = select_file()

    print("\nSpecify String:")
    search_string = specify_string()

    filtered_lines = extract_lines(lines, search_string)

    output_file = input("Output file: ")

    write_to_file(filtered_lines, output_file)

    print(f"Filtered lines containing '{search_string}' have been written to '{output_file}'.")


if __name__ == "__main__":
    main()
