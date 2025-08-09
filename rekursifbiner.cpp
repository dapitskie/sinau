#include <iostream>
#include <string>
using namespace std;

string biner2(int n) {
    if(n == 0){
        return "";
    } else {
        return biner2(n /2) + to_string(n%2);
}}

string biner(int n) {
    if(n == 0){
        return "0";
    } else {
        return biner2(n);
}}

// Fungsi main() di bawah tidak boleh diubah!
int main() {
    cout << biner(0) << endl;
    cout << biner(1) << endl;
    cout << biner(512) << endl;
    cout << biner(1697) << endl;
    cout << biner(1048575) << endl;
}
