#include <iostream>
#include <string>
#include <vector>
using namespace std;

string kalkulator(char op, vector<string> data) {
    vector<int> angka;
    for (string x : data) {
        angka.push_back(stoi(x));  // ubah int ke string
    }
    int hasil = angka[0];
    for (int i = 1; i < angka.size(); i++) {
        if (op == '+') {
            hasil += angka[i];
        } else if (op == '*') {
            hasil *= angka[i];
        } else {
            return "KESALAHAN";
        }
    }
    return to_string(hasil);  // ubah string ke int
}

// Fungsi main() di bawah tidak boleh diubah!
int main() {
    cout << kalkulator('+', {"1234567890", "0", "987654321", "314159265"}) << endl;
    cout << kalkulator('+', {"123", "456", "789", "111"}) << endl;
    cout << kalkulator('*', {"123", "456", "789", "111"}) << endl;
    cout << kalkulator('*', {"17", "8", "1945"}) << endl;
    cout << kalkulator('?', {"3", "2", "1"}) << endl;
}
