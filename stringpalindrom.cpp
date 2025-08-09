#include <iostream>
#include <string>
using namespace std;

bool palindrom(string s) {
    int n = s.length();
    if (n <= 1) {
        return true; // String is empty or has one character
    }
    
    // Check if the first and last characters are the same
    if (s[0] != s[n - 1]) {
        return false; // Not a palindrome
    }
    
    // Recursively check the substring excluding the first and last characters
    return palindrom(s.substr(1, n - 2));
}

// Fungsi main() di bawah tidak boleh diubah!
int main() {
    cout << palindrom("") << endl;
    cout << palindrom("x") << endl;
    cout << palindrom("aa") << endl;
    cout << palindrom("ab") << endl;
    cout << palindrom("ini") << endl;
    cout << palindrom("itu") << endl;
    cout << palindrom("anna") << endl;
    cout << palindrom("ibu ratna antar ubi") << endl;
    cout << palindrom("rumah murah") << endl;
    cout << palindrom("aku suka rajawali bapak apabila wajar aku suka") << endl;
}
