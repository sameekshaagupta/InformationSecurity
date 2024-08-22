def rail_fence_encrypt(plain_text, num_rails):
    if num_rails == 1:
        return plain_text
    
    rails = ['' for _ in range(num_rails)]
    rail = 0
    direction = 1

    for char in plain_text:
        rails[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    cipher_text = ''.join(rails)
    return cipher_text

def rail_fence_decrypt(cipher_text, num_rails):
    if num_rails == 1:
        return cipher_text

    rails = [['' for _ in range(len(cipher_text))] for _ in range(num_rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        rails[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1

    index = 0
    for r in range(num_rails):
        for c in range(len(cipher_text)):
            if rails[r][c] == '*':
                rails[r][c] = cipher_text[index]
                index += 1
    
    rail = 0
    direction = 1
    result = []
    for i in range(len(cipher_text)):
        result.append(rails[rail][i])
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    return ''.join(result)

plain_text = "Sameeksha"
num_rails = 5

encrypted_text = rail_fence_encrypt(plain_text, num_rails)
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, num_rails)
print("Decrypted:", decrypted_text)
