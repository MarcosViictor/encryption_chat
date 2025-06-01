
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding 
from cryptography.hazmat.backends import default_backend
import os
import base64

AES_KEY_SIZE = 32  
IV_SIZE = 16     

def generate_key_from_password(password_string):
    key_bytes = password_string.encode('utf-8')
    if len(key_bytes) < AES_KEY_SIZE:
        key_bytes = key_bytes + b'\0' * (AES_KEY_SIZE - len(key_bytes))
    return key_bytes[:AES_KEY_SIZE]

def encrypt_message(key, plain_text): 
    iv = os.urandom(IV_SIZE)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plain_text.encode('utf-8')) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(iv + ciphertext)

def decrypt_message(key, encrypted_data_b64):
    """Descriptografa a mensagem."""
    iv_ciphertext = base64.b64decode(encrypted_data_b64)
    iv = iv_ciphertext[:IV_SIZE]
    ciphertext = iv_ciphertext[IV_SIZE:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografar
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remover padding PKCS7
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext_bytes = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext_bytes