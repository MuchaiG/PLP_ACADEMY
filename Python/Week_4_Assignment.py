def main():
    input_file = input("Enter the filename to read: ")
    output_file = "output.txt"

    try:
        with open(input_file, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return
    except IOError:
        print(f"Error: Could not read the file '{input_file}'.")
        return

    modified_data = [line.strip().upper() + " - modified" for line in data]

    with open(output_file, "w") as file:
        file.writelines("\n".join(modified_data))

    print(f"Modified data has been written to '{output_file}'.")

if __name__ == "__main__":
    main()
