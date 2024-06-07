from cryptography.fernet import Fernet
import os

# Function to load the key
def load_key():
    return open(os.path.join(os.path.dirname(__file__), '..', 'secret.key'), "rb").read()

# Function to decrypt the credentials
def decrypt_credentials():
    key = load_key()
    cipher_suite = Fernet(key)
    with open(os.path.join(os.path.dirname(__file__), '..', 'encrypted_credentials.txt'), "rb") as cred_file:
        encrypted_lines = cred_file.readlines()
        if len(encrypted_lines) < 3:
            raise ValueError("The encrypted_credentials.txt file does not contain enough lines.")
        encrypted_username = encrypted_lines[0].strip()
        encrypted_password = encrypted_lines[1].strip()
        encrypted_incorrect_password = encrypted_lines[2].strip()
        username = cipher_suite.decrypt(encrypted_username).decode()
        password = cipher_suite.decrypt(encrypted_password).decode()
        incorrect_password = cipher_suite.decrypt(encrypted_incorrect_password).decode()
        return username, password, incorrect_password

URL = "https://www.linkedin.com/login"
USERNAME, PASSWORD, INCORRECT_PASSWORD = decrypt_credentials()
