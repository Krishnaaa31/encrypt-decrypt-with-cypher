from flask import Flask, render_template, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

def substitution_cipher_encrypt(text, substitution_key):
    encrypted_text = ''.join(substitution_key.get(char, char) for char in text)
    return encrypted_text

def substitution_cipher_decrypt(encrypted_text, substitution_key):
    decryption_key = {v: k for k, v in substitution_key.items()}
    decrypted_text = ''.join(decryption_key.get(char, char) for char in encrypted_text)
    return decrypted_text

def double_encrypt(plaintext, caesar_shift, substitution_key):
    caesar_encrypted = caesar_cipher_encrypt(plaintext, caesar_shift)
    substitution_encrypted = substitution_cipher_encrypt(caesar_encrypted, substitution_key)
    return substitution_encrypted

def double_decrypt(ciphertext, caesar_shift, substitution_key):
    substitution_decrypted = substitution_cipher_decrypt(ciphertext, substitution_key)
    caesar_decrypted = caesar_cipher_decrypt(substitution_decrypted, caesar_shift)
    return caesar_decrypted

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    caesar_shift = int(request.form['caesar_shift'])
    
    # Substitution key for the simple substitution cipher
    substitution_key = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                        'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                        'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                        'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
                        'z': 'a'}
    
    logging.debug("Plaintext: {}".format(plaintext))
    logging.debug("Caesar Shift: {}".format(caesar_shift))
    
    ciphertext = double_encrypt(plaintext, caesar_shift, substitution_key)
    
    logging.debug("Ciphertext: {}".format(ciphertext))

    return render_template('index.html', result_encrypt=ciphertext)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    caesar_shift = int(request.form['caesar_shift_decrypt'])
    
    # Substitution key for the simple substitution cipher
    substitution_key = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
                        'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
                        'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
                        'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
                        'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
                        'z': 'a'}
    
    logging.debug("Ciphertext: {}".format(ciphertext))
    logging.debug("Caesar Shift for Decryption: {}".format(caesar_shift))
    
    decrypted_text = double_decrypt(ciphertext, caesar_shift, substitution_key)
    
    logging.debug("Decrypted Text: {}".format(decrypted_text))

    return render_template('index.html', result_decrypt=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)