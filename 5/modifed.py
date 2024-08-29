def extend_key(msg, key):
    """Extend the key to match the length of the message."""
    key_length = len(key)
    extended_key = (key * (len(msg) // key_length + 1))[:len(msg)]
    return extended_key

def encrypt_vigenere(msg, key):
    """Encrypt the message using the Vigenère cipher."""
    extended_key = extend_key(msg, key)
    encrypted_text = []

    for m_char, k_char in zip(msg, extended_key):
        if m_char.isalpha():
            base = ord('A') if m_char.isupper() else ord('a')
            shift = ord(k_char.upper()) - ord('A')
            encrypted_char = chr((ord(m_char) - base + shift) % 26 + base)
        else:
            encrypted_char = m_char
        encrypted_text.append(encrypted_char)
    
    return ''.join(encrypted_text)

def decrypt_vigenere(msg, key):
    """Decrypt the message using the Vigenère cipher."""
    extended_key = extend_key(msg, key)
    decrypted_text = []

    for m_char, k_char in zip(msg, extended_key):
        if m_char.isalpha():
            base = ord('A') if m_char.isupper() else ord('a')
            shift = ord(k_char.upper()) - ord('A')
            decrypted_char = chr((ord(m_char) - base - shift + 26) % 26 + base)
        else:
            decrypted_char = m_char
        decrypted_text.append(decrypted_char)
    
    return ''.join(decrypted_text)

# Example usage
text_to_encrypt = "Sameeksha Gupta"
key = "HACK"

encrypted_text = encrypt_vigenere(text_to_encrypt, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt_vigenere(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
