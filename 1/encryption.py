Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
plaintext = input("Enter your message")
key = int(input("Enter your key: "))
plaintext = plaintext.upper()
if key > 26:
    key = key % 26 
plaintext = list(plaintext)
for i in range(len(plaintext)):
    if plaintext[i] in Alphabets:
        plaintext[i] = Alphabets[(Alphabets.index(plaintext[i]) + key)]
print("Your encrypted message is", ''.join(plaintext))

encrypted = list(plaintext)
for i in range(len(encrypted)):
    if encrypted[i] in Alphabets:
        encrypted[i] = Alphabets[(Alphabets.index(encrypted[i]) - key)]
print("Your original message is", ''.join(encrypted))