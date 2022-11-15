# Caesar-cipher
 
Simple script to run Caesar cipher on text or text files.

Script also can be used for ROT13 all you have to do is set the key to 13.


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

for simple text

```
❯ python app.py -t "Hello world\!" -k 13
--|input text
Hello world!
--|ciphered text
Uryyb jbeyq!
--|key
13
```
for text files

```
❯ python app.py -f file.txt -k 13
done writing to cipher.txt
```
