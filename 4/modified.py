import math
import random
import string

key = "HACK"

def encryptMessage(msg):
    col = len(key)
    msg_len = len(msg)
    row = math.ceil(msg_len / col)
    
    # Randomized padding character
    padding_char = random.choice(string.ascii_letters)
    msg += padding_char * (row * col - msg_len)

    # Create the matrix in a zigzag pattern
    matrix = [['' for _ in range(col)] for _ in range(row)]
    index = 0
    direction = 1  # 1 means left to right, -1 means right to left

    for i in range(row):
        if direction == 1:
            for j in range(col):
                matrix[i][j] = msg[index]
                index += 1
        else:
            for j in range(col - 1, -1, -1):
                matrix[i][j] = msg[index]
                index += 1
        direction *= -1  # Change direction

    # Dynamically determine column order based on ASCII values
    key_order = sorted(range(len(key)), key=lambda k: ord(key[k]))
    cipher = ''.join(''.join(matrix[i][j] for i in range(row)) for j in key_order)

    return cipher

def decryptMessage(cipher):
    col = len(key)
    msg_len = len(cipher)
    row = math.ceil(msg_len / col)

    # Dynamically determine column order based on ASCII values
    key_order = sorted(range(len(key)), key=lambda k: ord(key[k]))
    rev_key_order = sorted(range(len(key_order)), key=lambda k: key_order[k])

    # Create the matrix for decryption with reversed zigzag pattern
    matrix = [['' for _ in range(col)] for _ in range(row)]
    index = 0

    for j in key_order:
        for i in range(row):
            matrix[i][j] = cipher[index]
            index += 1

    # Reconstruct the original message with zigzag pattern
    msg = ''
    direction = 1  # 1 means left to right, -1 means right to left

    for i in range(row):
        if direction == 1:
            for j in range(col):
                msg += matrix[i][j]
        else:
            for j in range(col - 1, -1, -1):
                msg += matrix[i][j]
        direction *= -1  # Change direction

    return msg.rstrip(msg[-1])  # Remove padding character

msg = "Sameeksha Gupta"
cipher = encryptMessage(msg)
print("Encrypted Message: {}".format(cipher))
print("Decrypted Message: {}".format(decryptMessage(cipher)))
