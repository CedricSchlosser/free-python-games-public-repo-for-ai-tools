"""
Crypto, a tool for encrypting, decrypting and decoding messages.

Written by Grant Jenks
http://www.grantjenks.com/

Based on the Caesar Cipher algorithm from:
http://inventwithpython.com/chapter14.html

Copyright (c) 2014 Grant Jenks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

Exercises
0. Review 'ord' and 'chr' functions and letter-to-number mapping.
1. Explain what happens if you use key 26.
2. Find a way to decode a message without a key.
3. Encrypt numbers.
4. Make the encryption harder to decode.
"""

def encrypt(message, key):
    result = ''

    # Iterate letters in message and encrypt each individually.

    for letter in message:
        if letter.isalpha():

            # Letters are numbered like so:
            # A, B, C - Z is 65, 66, 67 - 90
            # a, b, c - z is 97, 98, 99 - 122

            num = ord(letter)

            if letter.isupper():
                base = ord('A')
            elif letter.islower():
                base = ord('a')

            # The encryption equation:

            num = (num - base + key) % 26 + base

            result += chr(num)

        elif letter.isdigit():

            # TODO: Encrypt digits.
            result += letter

        else:
            result += letter

    return result

def decrypt(message, key):
    return encrypt(message, -key)

def decode(message):
    # TODO: Decode a message without a key.
    pass

def get_message():
    print 'Enter a message:'
    message = raw_input()
    return message

def get_key():
    print 'Enter a key (1 - 25):'
    try:
        key = int(raw_input())
        return key
    except:
        print 'Invalid key. Using key: 0.'
        return 0

if __name__ == '__main__':
    print 'Do you wish to encrypt or decrypt or decode a message?'
    choice = raw_input()

    if choice == 'encrypt':

        message = get_message()
        key = get_key()
        print 'Encrypted message:'
        print encrypt(message, key)

    elif choice == 'decrypt':

        message = get_message()
        key = get_key()
        print 'Decrypted message:'
        print decrypt(message, key)

    elif choice == 'decode':

        message = get_message()
        print 'Decoding message:'
        decode(message)

    else:

        print 'Error: Unrecognized Command'
