alphabet =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
plaintext = input("Enter the message:");
key = int(input("Enter the key:"));
plaintext=plaintext.upper();
if key>26:
    key = key%26;
plaintext = list(plaintext);
for i in range(len(plaintext)):
    if plaintext[i] in alphabet:
        if i==0:
            plaintext[i] = alphabet[(alphabet.index(plaintext[i])+key+1)];
        elif i%2==0:
            plaintext[i] = alphabet[(alphabet.index(plaintext[i])+key+1)];
        else:
            plaintext[i] = alphabet[(alphabet.index(plaintext[i])+key-1)];
print("Encrypted message:", ''.join(plaintext))

encrypted = list(plaintext);
for i in range(len(encrypted)):
    if encrypted[i] in alphabet:
        if i==0:
            encrypted[i] = alphabet[(alphabet.index(plaintext[i])-key-1)];
        elif i%2==0:
            encrypted[i] = alphabet[(alphabet.index(plaintext[i])-key-1)];
        else:
            encrypted[i] = alphabet[(alphabet.index(plaintext[i])-key+1)];
print("Original message:",''.join(encrypted))