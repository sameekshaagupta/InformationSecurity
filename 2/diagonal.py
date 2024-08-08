def diagonal_playfair_cipher(plaintext, key, mode):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    key = key.lower().replace(' ', '').replace('j', 'i')
    
    key_square = ''
    for letter in key + alphabet:
        if letter not in key_square:
            key_square += letter
    
    plaintext = plaintext.lower().replace(' ', '').replace('j', 'i')
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    
    def find_position(letter):
        index = key_square.index(letter)
        return divmod(index, 5)
    
    def encrypt(digraph):
        a, b = digraph
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)
        if row_a == row_b:
            row_a = (row_a - 1) % 5
            col_a = (col_a + 1) % 5
            row_b = (row_b - 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5
            col_a = (col_a + 1) % 5
            row_b = (row_b + 1) % 5
            col_b = (col_b + 1) % 5
        else:
            row_a, col_a = (row_a - 1) % 5, (col_a + 1) % 5
            row_b, col_b = (row_b - 1) % 5, (col_b + 1) % 5
        return key_square[row_a*5 + col_a] + key_square[row_b*5 + col_b]
    
    def decrypt(digraph):
        a, b = digraph
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)
        if row_a == row_b:
            row_a = (row_a + 1) % 5
            col_a = (col_a - 1) % 5
            row_b = (row_b + 1) % 5
            col_b = (col_b - 1) % 5
        elif col_a == col_b:
            row_a = (row_a - 1) % 5
            col_a = (col_a - 1) % 5
            row_b = (row_b - 1) % 5
            col_b = (col_b - 1) % 5
        else:
            row_a, col_a = (row_a + 1) % 5, (col_a - 1) % 5
            row_b, col_b = (row_b + 1) % 5, (col_b - 1) % 5
        return key_square[row_a*5 + col_a] + key_square[row_b*5 + col_b]
    
    result = ''
    for digraph in digraphs:
        if mode == 'encrypt':
            result += encrypt(digraph)
        elif mode == 'decrypt':
            result += decrypt(digraph)
    
    return result

# Example usage
plaintext = 'Sameeksha'
key = ''
ciphertext = diagonal_playfair_cipher(plaintext, key, 'encrypt')
print("encrypted:",ciphertext)
decrypted_text = diagonal_playfair_cipher(ciphertext, key, 'decrypt')
print("decrypted:",decrypted_text)
