#include <bits/stdc++.h>
using namespace std;

string encrypt(const string& text, const string& key) {
    string result = "";
    int keyLength = key.length();
    int keyIndex = 0;

    for (char ch : text) {
        if (isalpha(ch)) {
            char shift = key[keyIndex % keyLength] - 'a';
            char encryptedChar = (ch - 'a' + shift) % 26 + 'a';
            result += encryptedChar;
            keyIndex++;
        } else {
            result += ch;
        }
    }
    return result;
}

string decrypt(const string& text, const string& key) {
    string result = "";
    int keyLength = key.length();
    int keyIndex = 0;

    for (char ch : text) {
        if (isalpha(ch)) {
            char shift = key[keyIndex % keyLength] - 'a';
            char decryptedChar = (ch - 'a' - shift + 26) % 26 + 'a';
            result += decryptedChar;
            keyIndex++;
        } else {
            result += ch;
        }
    }
    return result;
}

int main() {
    string text, key;
    cout << "Sameeksha Gupta\n22BCP343\n";
    cout << "Enter the text: ";
    getline(cin, text);

    cout << "Enter the key: ";
    getline(cin, key);

    string encryptedText = encrypt(text, key);
    string decryptedText = decrypt(encryptedText, key);

    cout << "Encrypted text: " << encryptedText << endl;
    cout << "Decrypted text: " << decryptedText << endl;

    return 0;
}

