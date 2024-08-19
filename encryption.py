from cryptography.fernet import Fernet

# Generate a key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt data
def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Decrypt data
def decrypt_data(encrypted_data):
    key = load_key()
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

# Example usage
generate_key()
encrypted = encrypt_data("Sensitive Information")
print(f"Encrypted: {encrypted}")
decrypted = decrypt_data(encrypted)
print(f"Decrypted: {decrypted}")