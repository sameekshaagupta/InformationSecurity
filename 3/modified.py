def rail_fence_encrypt(plain_text, num_rails, direction='down'):
    if num_rails == 1:
        return plain_text

    rails = ['' for _ in range(num_rails)]
    rail = 0
    dir = 1 if direction == 'down' else -1

    for char in plain_text:
        rails[rail] += char
        rail += dir
        if rail == num_rails or rail < 0:
            dir *= -1
            rail += dir

    return ''.join(rails)

def rail_fence_decrypt(cipher_text, num_rails, direction='down'):
    if num_rails == 1:
        return cipher_text

    # Create a matrix with placeholders
    rails = [['' for _ in range(len(cipher_text))] for _ in range(num_rails)]
    rail = 0
    dir = 1 if direction == 'down' else -1

    # Mark the positions in the matrix
    for i in range(len(cipher_text)):
        rails[rail][i] = '*'
        rail += dir
        if rail == num_rails or rail < 0:
            dir *= -1
            rail += dir

    # Fill the matrix with cipher text characters
    index = 0
    for r in range(num_rails):
        for c in range(len(cipher_text)):
            if rails[r][c] == '*':
                rails[r][c] = cipher_text[index]
                index += 1

    # Read the matrix in zigzag pattern to get the decrypted text
    result = []
    rail = 0
    dir = 1 if direction == 'down' else -1

    for i in range(len(cipher_text)):
        result.append(rails[rail][i])
        rail += dir
        if rail == num_rails or rail < 0:
            dir *= -1
            rail += dir

    return ''.join(result)

# Example Usage
plain_text = "Sameeksha"
num_rails = 5

# Encrypting with default direction ('down')
encrypted_text = rail_fence_encrypt(plain_text, num_rails)
print("Encrypted (down):", encrypted_text)

# Decrypting with default direction ('down')
decrypted_text = rail_fence_decrypt(encrypted_text, num_rails)
print("Decrypted (down):", decrypted_text)

# Encrypting with 'up' direction
encrypted_text_up = rail_fence_encrypt(plain_text, num_rails, direction='up')
print("Encrypted (up):", encrypted_text_up)

# Decrypting with 'up' direction
decrypted_text_up = rail_fence_decrypt(encrypted_text_up, num_rails, direction='up')
print("Decrypted (up):", decrypted_text_up)
