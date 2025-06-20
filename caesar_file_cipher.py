def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Main function
def main():
    print("File-based Caesar Cipher")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Exiting.")
        return

    input_file = input("Enter the input filename (e.g., input.txt): ")
    output_file = input("Enter the output filename (e.g., output.txt): ")
    shift = int(input("Enter the shift value (integer): "))

    try:
        with open(input_file, 'r') as file:
            message = file.read()

        if choice == 'e':
            result = caesar_cipher(message, shift)
        else:
            result = caesar_cipher(message, -shift)

        with open(output_file, 'w') as file:
            file.write(result)

        print(f"Operation successful! Output written to '{output_file}'.")

    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
