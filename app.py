import argparse


def encrypt(char: str, key: int, mode: bool = True):
    """encrypts a single character

    Args:
        char (str): character
        key (int): shift number
        mode (bool, optional): True for encryption, False for decryption. Defaults to True.

    Returns:
        str: ciphered character
    """
    if char.isalpha():
        char_ascii = ord(char)
        mod = 96 if char.islower() else 64

        if mode:
            ciphered_ascii = (char_ascii + key) % mod
        else:
            ciphered_ascii = (char_ascii - key) % mod

        if ciphered_ascii > 26:
            ciphered_ascii -= 26

        return chr(ciphered_ascii + mod)
    else:
        return char


def caesar(text: str, key: int, mode: bool = True):
    # function for string of text
    cipher = ""

    for char in text:
        cipher += encrypt(char, key, mode)

    return cipher


def caesar_file(file: str, key: int, mode: bool = True):
    # function for a file
    cipher = ""

    with open(file, "r", encoding="ascii") as file:
        for line in file:
            for char in line:
                cipher += encrypt(char, key, mode)

    with open("cipher.txt", "w", encoding="ascii") as cipher_file:
        cipher_file.write(cipher)


def setup_argparse():
    parser = argparse.ArgumentParser(description="script for caesar cipher")

    input_mode = parser.add_mutually_exclusive_group(required=True)
    input_mode.add_argument("-t", "--text", type=str,
                            metavar="", help="input text")
    input_mode.add_argument("-f", "--file", type=str,
                            metavar="", help="file name (e.g. file.txt)")

    parser.add_argument("-k", "--key", type=int, metavar="", help="shift key")

    arg_mode = parser.add_mutually_exclusive_group()
    arg_mode.add_argument(
        "-e", "--encrypt", action="store_true", help="run script in encryption mode (default)")
    arg_mode.add_argument(
        "-d", "--decrypt", action="store_true", help="run script in decryption mode")

    return parser.parse_args()


def main():
    # main function that you use to run the program
    args = setup_argparse()

    plain_text = args.text
    file_name = args.file
    key = abs(args.key)
    script_mode = not args.decrypt

    if plain_text:
        output_text = caesar(plain_text, key, script_mode)
        print("--|input text", plain_text,
              "--|ciphered text", output_text,
              "--|key", key,
              sep="\n")
    elif file_name:
        caesar_file("file.txt", key, script_mode)
        output_text = "done writing to cipher.txt"
        print(output_text)


if __name__ == "__main__":
    main()
