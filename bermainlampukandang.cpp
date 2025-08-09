#include <iostream>
using namespace std;

int main() {
    bool lampu[101];

    // Pada mulanya, seluruh lampu dalam kondisi mati.
    for (int i = 1; i <= 100; i++) {
        lampu[i] = false;
    }

    // Untuk setiap jam (pukul p),
    for (int p = 1;  p <= 100; p++) {
        // untuk setiap lampu nomor i,
        for (int i = 1; i <= 100; i++) {
            // jika i merupakan kelipatan p,
            if (i % p == 0) {
                // tekan saklarnya.
                lampu[i] = !lampu[i]; // Toggle the state of the lamp
            }
        }
    }

    // Hitung banyaknya lampu yang menyala,
    int menyala = 0;
    for (int i = 1; i <= 100; i++) {
        if (lampu[i]) {
            menyala++;
        }
    }

    // lalu cetak.
    cout << menyala;
}
