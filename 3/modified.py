def diagonal_rail_fence_encrypt(plain_text, num_rails):
    if num_rails == 1:
        return plain_text
    
    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1

    for char in plain_text:
        rails[rail] += char
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction *= -1
    
    # Place characters in a diagonal pattern
    diagonal_pattern = ['' for _ in range(num_rails)]
    index = 0
    for i in range(len(plain_text)):
        rail_index = (index % num_rails)
        diagonal_pattern[rail_index] += plain_text[i]
        index += 1

    cipher_text = ''.join(diagonal_pattern)
    return cipher_text

def diagonal_rail_fence_decrypt(cipher_text, num_rails):
    if num_rails == 1:
        return cipher_text
    
    rails = [['' for _ in range(len(cipher_text))] for _ in range(num_rails)]
    rail = 0
    direction = 1
    pattern_indices = [[None for _ in range(len(cipher_text))] for _ in range(num_rails)]

    for i in range(len(cipher_text)):
        pattern_indices[rail][i] = '*'
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction *= -1
    
    index = 0
    for r in range(num_rails):
        for c in range(len(cipher_text)):
            if pattern_indices[r][c] == '*':
                pattern_indices[r][c] = cipher_text[index]
                index += 1
    
    rail = 0
    direction = 1
    result = []
    for i in range(len(cipher_text)):
        result.append(pattern_indices[rail][i])
        rail += direction
        if rail == num_rails - 1 or rail == 0:
            direction *= -1
    
    return ''.join(result)

# Example usage
plain_text = "Sameeksha"
num_rails = 5

encrypted_text = diagonal_rail_fence_encrypt(plain_text, num_rails)
print("Encrypted:", encrypted_text)

decrypted_text = diagonal_rail_fence_decrypt(encrypted_text, num_rails)
print("Decrypted:", decrypted_text)
