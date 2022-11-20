# Caesar-cipher

A simple script to run Caesar cipher on text or text files.

Script can also be used for ROT13, all you have to do is set the key to 13.

## Installation

Download or clone this repository and enter the main folder. Python 3 is required to
run the application.

## Usage

```
❯ python app.py -h
usage: app.py [-h] (-t  | -f ) [-k] [-e | -d]

script for caesar cipher

options:
  -h, --help     show this help message and exit
  -t, --text     input text
  -f, --file     file name (e.g. file.txt)
  -k, --key      shift key
  -e, --encrypt  run script in encryption mode (default)
  -d, --decrypt  run script in decryption mode
```
### Examples

String
```
❯ python app.py -t "Hello world\!" -k 13
--|input text
Hello world!
--|ciphered text
Uryyb jbeyq!
--|key
13
```

Text file

```
❯ python app.py -f file.txt -k 13
done writing to cipher.txt

# Original file
❯ head file.txt
a b c d e f g h i j k l m n o p q r s t u v w x y z .!@#$%^&*()_+\UwU/
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z .!@#$%^&*()_+\UwU/

# Ciphered file
❯ head cipher.txt
n o p q r s t u v w x y z a b c d e f g h i j k l m .!@#$%^&*()_+\HjH/
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M .!@#$%^&*()_+\HjH/ 
```