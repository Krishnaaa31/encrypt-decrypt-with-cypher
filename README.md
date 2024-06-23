# encrypt-decrypt-with-cypher
 Double Encryption Decryption Flask App 
# Double Encryption Flask App

This repository contains a Python Flask web application that performs double encryption and decryption using a combination of Caesar cipher and substitution cipher. The app allows users to encrypt and decrypt text inputs via a web interface.

## Key Features

- **Caesar Cipher**: Encrypts and decrypts text by shifting characters by a specified number of positions in the alphabet.
- **Substitution Cipher**: Encrypts and decrypts text by replacing each character with another character according to a specified key.
- **Double Encryption/Decryption**: Combines both Caesar and substitution ciphers for enhanced security.

## Libraries Used

- **Flask**: For creating the web application.
- **logging**: For debugging and logging application events.

## Getting Started

1. Clone the repository.
2. Install Flask: `pip install Flask`.
3. Run the application: `python app.py`.
4. Open your browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Encrypt Text**: 
   - Enter plaintext and Caesar shift value.
   - The app will apply Caesar cipher followed by substitution cipher.
2. **Decrypt Text**:
   - Enter ciphertext and the same Caesar shift value used for encryption.
   - The app will reverse the substitution cipher followed by the Caesar cipher.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
